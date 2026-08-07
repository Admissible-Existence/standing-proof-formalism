#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "standing-proof-principle-completeness-validation.json"
REQUIRED_FILES = [
    "README.md",
    "docs/STANDING_PROOF_FORMALISM_MIRROR_HANDOFF.md",
    "docs/STANDING_PROOF_MIRROR_HANDOFF.md",
    "docs/WHOLE_REPO_THEORY_MAP.md",
    "docs/MATHEMATICAL_NOTATION.md",
    "docs/FALSIFICATION_AND_LIMITS.md",
    "formalism/principle-registry.yaml",
    "formalism/dependency-graph.yaml",
    "formalism/proof-candidates.yaml",
    "data/standing-surfaces.json",
    "data/standing-results.json",
    "data/standing-integration.json",
    "data/standing-cases.json",
    "tools/check_standing_surfaces.py",
    "tools/check_standing_results.py",
    "tools/check_standing_integration.py",
    "tools/check_standing_cases.py",
]
CHECKS = [
    "tools/check_standing_surfaces.py",
    "tools/check_standing_results.py",
    "tools/check_standing_integration.py",
    "tools/check_standing_cases.py",
]
PRINCIPLES = ["SPF-P-001", "SPF-P-002", "SPF-P-003", "SPF-P-004"]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(relative: str) -> dict:
    completed = subprocess.run(
        [sys.executable, str(ROOT / relative)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "command": relative,
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def main() -> int:
    findings = []
    missing = [relative for relative in REQUIRED_FILES if not (ROOT / relative).is_file()]
    if missing:
        findings.append({"kind": "missing_required_files", "paths": missing})

    registry = ROOT / "formalism" / "principle-registry.yaml"
    if registry.is_file():
        text = registry.read_text(encoding="utf-8")
        absent = [pid for pid in PRINCIPLES if pid not in text]
        if absent:
            findings.append({"kind": "missing_principles", "ids": absent})
        if "authority_effect: false" not in text:
            findings.append({"kind": "authority_boundary_missing"})

    compact_authority = {}
    for relative in ["data/standing-surfaces.json", "data/standing-results.json", "data/standing-integration.json", "data/standing-cases.json"]:
        path = ROOT / relative
        if path.is_file():
            payload = json.loads(path.read_text(encoding="utf-8"))
            compact_authority[relative] = payload.get("authority")
            if payload.get("authority") is not False:
                findings.append({"kind": "authority_escalation", "path": relative})

    subchecks = [run(relative) for relative in CHECKS]
    for check in subchecks:
        if check["returncode"] != 0:
            findings.append({"kind": "failed_subcheck", "command": check["command"]})

    input_sha256 = {
        relative: sha256(ROOT / relative)
        for relative in REQUIRED_FILES
        if (ROOT / relative).is_file()
    }

    case_payload = json.loads((ROOT / "data" / "standing-cases.json").read_text(encoding="utf-8")) if (ROOT / "data" / "standing-cases.json").is_file() else {"cases": []}
    receipt = {
        "schema_version": "admissible_existence.standing.principle_completeness_receipt.v1",
        "repository": "Admissible-Existence/standing-proof-formalism",
        "goal_id": "STANDING-PROOF-PRINCIPLE-COMPLETENESS-001",
        "principle_count": len(PRINCIPLES),
        "expected_principle_count": 4,
        "standing_case_count": len(case_payload.get("cases", [])),
        "subchecks": subchecks,
        "input_sha256": input_sha256,
        "compact_authority": compact_authority,
        "findings": findings,
        "execution_authorized": False,
        "publication_authorized": False,
        "proofs_accepted": False,
        "claims_final_cross_repository_validity": False,
        "prior_review_inherits_standing": False,
        "valid": not findings,
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
