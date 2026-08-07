from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "data" / "standing-cases.json"
REQUIRED = {"actor", "target", "scope", "policy", "delegation", "evidence", "context", "validity_window", "recoverability"}
ALLOWED_STATES = {"VALID", "INVALID", "UNKNOWN"}
ALLOWED_RESULTS = {"ALLOW", "DENY", "FAIL_CLOSED", "INCOMPLETE"}


def evaluate(surfaces):
    if not isinstance(surfaces, dict):
        return "FAIL_CLOSED"
    if set(surfaces) != REQUIRED:
        return "FAIL_CLOSED"
    values = list(surfaces.values())
    if any(value not in ALLOWED_STATES for value in values):
        return "FAIL_CLOSED"
    if any(value == "UNKNOWN" for value in values):
        return "INCOMPLETE"
    if any(value == "INVALID" for value in values):
        return "DENY"
    return "ALLOW"


def main():
    if not CASES.exists():
        print("missing: data/standing-cases.json")
        return 1
    data = json.loads(CASES.read_text(encoding="utf-8"))
    errors = []
    if data.get("schema") != "admissible_existence.standing.cases.v1":
        errors.append("unexpected schema")
    if data.get("repo") != "standing-proof-formalism":
        errors.append("unexpected repo")
    if data.get("authority") is not False:
        errors.append("case fixture cannot create authority")
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        errors.append("cases missing")
        cases = []
    seen = set()
    for case in cases:
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id or case_id in seen:
            errors.append(f"invalid or duplicate case id: {case_id}")
            continue
        seen.add(case_id)
        expected = case.get("expected")
        if expected not in ALLOWED_RESULTS:
            errors.append(f"{case_id}: invalid expected result")
            continue
        actual = evaluate(case.get("surfaces"))
        if actual != expected:
            errors.append(f"{case_id}: expected {expected}, got {actual}")
    print(json.dumps({"valid": not errors, "case_count": len(cases), "errors": errors}, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
