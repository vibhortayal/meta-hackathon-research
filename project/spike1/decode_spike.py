#!/usr/bin/env python3
"""Spike 1 v1: decode Costco receipt texts with muse-spark-1.3 (Standard only — real personal data).
Reads spike1/texts/*.txt, writes spike1/results/<name>.json, prints per-receipt scorecard."""
import glob, importlib.util, json, os, sys

spec = importlib.util.spec_from_file_location("meta_api", os.path.expanduser("~/workspace/custom-connectors/custom.meta-model-api/bin/meta_api.py"))
meta = importlib.util.module_from_spec(spec); spec.loader.exec_module(meta)

SYSTEM = """You decode Costco warehouse receipt text extracted from a PDF. The text layer is jumbled: product descriptions wrap across fragments and columns interleave, so a line's words may appear on neighbouring lines. Reconstruct each purchased line item.

Return ONLY a JSON object, no prose:
{"store": str, "date": str, "lines": [{"item_no": str, "product": str, "brand": str|null, "detail": str|null, "price": number, "qty": number, "is_return": bool, "confidence": number 0..1, "needs_user_check": bool, "alternatives": [str]}], "subtotal": number, "tax": number, "total": number, "items_sold": number}

Rules:
- "KS" = Kirkland Signature (Costco's brand). Expand abbreviations (ORG=organic, BLUES=blueberries, etc.) only when confident.
- qty: lines like "2 @ 79.99" mean qty 2 at that unit price; price = the line total.
- A return/refund line has a negative price or REFUND wording: set is_return true.
- confidence: your honest probability the product identification is exactly right. If below 0.8, set needs_user_check true and give up to 2 alternatives.
- Do not invent lines. If fragments cannot be assigned, still emit the line with your best reading, low confidence, needs_user_check true.
- items_sold and the money fields come from the receipt footer."""

def main():
    files = sorted(glob.glob(os.path.expanduser("~/workspace/meta-hackathon-2026/spike1/texts/*.txt")))
    grand = {"receipts": 0, "lines": 0, "auto": 0, "check": 0, "arith_ok": 0}
    for path in files:
        text = open(path).read()
        body = {"model": "muse-spark-1.3", "temperature": 0.1,
                "messages": [{"role": "system", "content": SYSTEM},
                             {"role": "user", "content": "Decode this receipt text:\n\n" + text}]}
        status, payload = meta.call("POST", "/v1/chat/completions", body)
        name = os.path.splitext(os.path.basename(path))[0]
        out = {"http_status": status, "file": name}
        if status == 200:
            content = payload["choices"][0]["message"]["content"]
            usage = payload.get("usage", {})
            out["usage"] = usage
            try:
                dec = json.loads(content)
            except Exception:
                start, end = content.find("{"), content.rfind("}")
                dec = json.loads(content[start:end+1])
            out["decoded"] = dec
            lines = dec.get("lines", [])
            ssum = round(sum(l["price"] for l in lines if not l.get("is_return")), 2)
            arith = abs(ssum - float(dec.get("subtotal", -1))) <= 0.05
            auto = sum(1 for l in lines if not l.get("needs_user_check"))
            grand["receipts"] += 1; grand["lines"] += len(lines); grand["auto"] += auto
            grand["check"] += len(lines) - auto; grand["arith_ok"] += 1 if arith else 0
            print(f"{name}: {dec.get('store')} {dec.get('date')} lines={len(lines)} (receipt says {dec.get('items_sold')}) "
                  f"auto={auto} check={len(lines)-auto} sum={ssum} vs subtotal={dec.get('subtotal')} arith={'OK' if arith else 'MISMATCH'} usage={usage}")
            for l in lines:
                if l.get("needs_user_check"):
                    print(f"   CHECK: {l.get('item_no')} -> {l.get('product')} conf={l.get('confidence')} alts={l.get('alternatives')}")
        else:
            out["error"] = payload
            print(f"{name}: HTTP {status} ERROR {json.dumps(payload)[:300]}")
        json.dump(out, open(os.path.expanduser(f"~/workspace/meta-hackathon-2026/spike1/results/{name}.json"), "w"), indent=2)
    print("TOTALS:", json.dumps(grand))

if __name__ == "__main__":
    main()
