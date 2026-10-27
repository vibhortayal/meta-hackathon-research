#!/usr/bin/env python3
import base64, importlib.util, json, os, sys
spec = importlib.util.spec_from_file_location("meta_api", os.path.expanduser("~/workspace/custom-connectors/custom.meta-model-api/bin/meta_api.py"))
meta = importlib.util.module_from_spec(spec); spec.loader.exec_module(meta)
src = open(os.path.expanduser("~/workspace/meta-hackathon-2026/spike2/decode_photo.py")).read()
SYSTEM = src.split('SYSTEM = """')[1].split('"""')[0]
path = sys.argv[1]
name = os.path.splitext(os.path.basename(path))[0]
b64 = base64.b64encode(open(path, "rb").read()).decode()
body = {"model": "muse-spark-1.3", "temperature": 0.1,
        "messages": [{"role": "system", "content": SYSTEM},
                     {"role": "user", "content": [{"type": "text", "text": "Decode this receipt photo."},
                                                  {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64," + b64}}]}]}
status, payload = meta.call("POST", "/v1/chat/completions", body)
out = {"http_status": status, "file": name}
if status == 200:
    content = payload["choices"][0]["message"]["content"]
    out["usage"] = payload.get("usage", {})
    try: dec = json.loads(content)
    except Exception: dec = json.loads(content[content.find("{"):content.rfind("}")+1])
    out["decoded"] = dec
    lines = dec.get("lines", [])
    print(f"== {name}: {dec.get('store')} {dec.get('date')} lines={len(lines)} (says {dec.get('items_sold')}) sum={round(sum(l['price'] for l in lines),2)} subtotal={dec.get('subtotal')} total={dec.get('total')} usage={out['usage']}")
    for l in lines:
        print(f"   {l.get('item_no')} | {l.get('brand')} {l.get('product')} {l.get('detail') or ''} | list {l.get('list_price')} paid {l.get('price')} disc {l.get('discount')} qty {l.get('qty')} | conf {l.get('confidence')}{' CHECK' if l.get('needs_user_check') else ''} alts={l.get('alternatives')}")
else:
    out["error"] = payload; print(name, "HTTP", status, json.dumps(payload)[:300])
base = os.path.expanduser("~/workspace/meta-hackathon-2026/spike2")
json.dump(out, open(f"{base}/results/{name}.json", "w"), indent=2)
print("DONE")
