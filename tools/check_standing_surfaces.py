from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "data" / "standing-surfaces.json"
required = {"actor", "target", "scope", "policy", "delegation", "evidence", "context", "validity_window", "recoverability"}
ok = path.exists()
if ok:
    data = json.loads(path.read_text(encoding="utf-8"))
    ok = ok and data.get("schema") == "admissible_existence.standing.surfaces.v1"
    ok = ok and data.get("repo") == "standing-proof-formalism"
    ok = ok and required.issubset(set(data.get("surfaces", [])))
    ok = ok and data.get("status") == "surfaces_ready"
    ok = ok and data.get("authority") is False
else:
    print("missing: data/standing-surfaces.json")
print("valid: standing surfaces" if ok else "standing surfaces check failed")
raise SystemExit(0 if ok else 1)
