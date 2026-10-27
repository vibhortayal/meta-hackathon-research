#!/usr/bin/env python3
import glob, importlib.util, json, os
spec = importlib.util.spec_from_file_location("ds", os.path.expanduser("~/workspace/meta-hackathon-2026/spike1/decode_spike.py"))
# decode_spike runs main only under __main__; re-declare SYSTEM + call here instead
import importlib.util as iu
mspec = iu.spec_from_file_location("meta_api", os.path.expanduser("~/workspace/custom-connectors/custom.meta-model-api/bin/meta_api.py"))
meta = iu.module_from_spec(mspec); mspec.loader.exec_module(meta)
src = open(os.path.expanduser("~/workspace/meta-hackathon-2026/spike1/decode_spike.py")).read()
SYSTEM = src.split('SYSTEM = """')[1].split('"""')[0]
base = os.path.expanduser("~/workspace/meta-hackathon-2026/spike1")
for path in sorted(glob.glob(base + "/texts/*.txt")):
    name = os.path.splitext(os.path.basename(path))[0]
    outp = f"{base}/results/{name}.json"
    if os.path.exists(outp) and "decoded" in json.load(open(outp)):
        print(name, "already decoded, skip"); continue
    text = open(path).read()
    body = {"model": "muse-spark-1.3", "temperature": 0.1,
            "messages": [{"role": "system", "content": SYSTEM},
                         {"role": "user", "content": "Decode this receipt text:\n\n" + text}]}
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
        ssum = round(sum(l["price"] for l in lines if not l.get("is_return")), 2)
        print(f"{name}: lines={len(lines)} (says {dec.get('items_sold')}) sum={ssum} vs subtotal={dec.get('subtotal')}")
    else:
        out["error"] = payload; print(name, "HTTP", status)
    json.dump(out, open(outp, "w"), indent=2)
print("DONE")
