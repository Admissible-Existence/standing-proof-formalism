from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "data" / "standing-results.json"
required = {"ALLOW", "DENY", "FAIL_CLOSED", "INCOMPLETE"}
ok = path.exists()
if ok:
    data = json.loads(path.read_text(encoding="utf-8"))
    ok = ok and data.get("schema") == "admissible_existence.standing.results.v1"
    ok = ok and data.get("repo") == "standing-proof-formalism"
    ok = ok and required.issubset(set(data.get("results", [])))
    ok = ok and data.get("status") == "results_ready"
    ok = ok and data.get("authority") is False
else:
    print("missing: data/standing-results.json")
print("valid: standing results" if ok else "standing results check failed")
raise SystemExit(0 if ok else 1)
