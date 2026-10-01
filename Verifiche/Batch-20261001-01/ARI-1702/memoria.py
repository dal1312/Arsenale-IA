import json,sys
from pathlib import Path
p=Path(sys.argv[2])
if sys.argv[1]=="save":
 data={"preferenze":{"lingua":"italiano"},"conoscenza":{"fonte_canonica":"PROCEDURA.md"},"log":[{"evento":"memoria salvata"}]}
 with p.open("x",encoding="utf-8") as f: json.dump(data,f,ensure_ascii=False)
 print(json.dumps({"contesto_temporaneo_persistito":False,"segreti_persistiti":False}))
elif sys.argv[1]=="load":
 print(p.read_text(encoding="utf-8"))
else: raise SystemExit(2)
