#!/usr/bin/env python3
"""Spike 2 (photo gate) v1: decode receipt PHOTOS with muse-spark-1.3 vision (Standard only)."""
import base64, glob, importlib.util, json, os
spec = importlib.util.spec_from_file_location("meta_api", os.path.expanduser("~/workspace/custom-connectors/custom.meta-model-api/bin/meta_api.py"))
meta = importlib.util.module_from_spec(spec); spec.loader.exec_module(meta)

SYSTEM = """You decode a PHOTOGRAPH of a paper store receipt. The photo may be crumpled, curved, shadowed, rotated, or partly covered by a hand. Read what is visible; never invent what is not.

Return ONLY a JSON object, no prose:
{"store": str, "date": str, "lines": [{"item_no": str|null, "product": str, "brand": str|null, "detail": str|null, "list_price": number|null, "price": number, "discount": number, "qty": number, "is_return": bool, "confidence": number 0..1, "needs_user_check": bool, "alternatives": [str]}], "subtotal": number, "tax": number, "total": number, "items_sold": number}

Rules:
- Some receipts print two money columns: a list "Price" and a "You Pay" amount. "price" = the amount PAID (You Pay). "list_price" = the list price. If only one column exists, list_price = price.
- A savings/discount line printed under an item (e.g. "Member Savings -3.00", "INST SAV") belongs to that item: put its absolute value in "discount" and NEVER emit it as its own line.
- subtotal = sum of paid line prices. total = the balance amount paid. items_sold comes from the receipt footer when printed.
- Expand brand abbreviations only when confident (GG = Green Giant). Keep short flavor/variant codes (BR, CH, PI) in "detail" unexpanded unless you are confident; if below 0.8 confidence on the product identity, set needs_user_check true and give alternatives.
- If digits of an item number are hidden or unreadable, return the visible digits with null for the number if too uncertain, and lower the confidence.
- A return/refund has a negative amount: is_return true."""

base = os.path.expanduser("~/workspace/meta-hackathon-2026/spike2")
for path in sorted(glob.glob(base + "/photos/*.jpg")):
    name = os.path.splitext(os.path.basename(path))[0]
    b64 = base64.b64encode(open(path, "rb").read()).decode()
    body = {"model": "muse-spark-1.3", "temperature": 0.1,
            "messages": [{"role": "system", "content": SYSTEM},
                         {"role": "user", "content": [
                             {"type": "text", "text": "Decode this receipt photo."},
                             {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64," + b64}}]}]}
    status, payload = meta.call("POST", "/v1/chat/completions", body)
    out = {"http_status": status, "file": name}
    if status == 200:
        content = payload["choices"][0]["message"]["content"]
        out["usage"] = payload.get("usage", {})
        try: dec = json.loads(content)
        except Exception:
            dec = json.loads(content[content.find("{"):content.rfind("}")+1])
        out["decoded"] = dec
        lines = dec.get("lines", [])
        ssum = round(sum(l["price"] for l in lines), 2)
        print(f"== {name}: {dec.get('store')} {dec.get('date')} lines={len(lines)} (says {dec.get('items_sold')}) sum={ssum} subtotal={dec.get('subtotal')} total={dec.get('total')} usage={out['usage']}")
        for l in lines:
            print(f"   {l.get('item_no')} | {l.get('brand')} {l.get('product')} {l.get('detail') or ''} | list {l.get('list_price')} paid {l.get('price')} disc {l.get('discount')} | conf {l.get('confidence')}{' CHECK' if l.get('needs_user_check') else ''} alts={l.get('alternatives')}")
    else:
        out["error"] = payload
        print(f"== {name}: HTTP {status} {json.dumps(payload)[:400]}")
    json.dump(out, open(f"{base}/results/{name}.json", "w"), indent=2)
print("DONE")
