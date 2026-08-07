from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "data" / "standing-integration.json"
required = {"AE", "BC", "CHF", "DC", "DaCo", "StegVerse"}
ok = path.exists()
if ok:
    data = json.loads(path.read_text(encoding="utf-8"))
    ok = ok and data.get("schema") == "admissible_existence.standing.integration.v1"
    ok = ok and data.get("repo") == "standing-proof-formalism"
    ok = ok and required.issubset(set(data.get("links", [])))
    ok = ok and data.get("status") == "integration_ready"
    ok = ok and data.get("authority") is False
else:
    print("missing: data/standing-integration.json")
print("valid: standing integration" if ok else "standing integration check failed")
raise SystemExit(0 if ok else 1)
