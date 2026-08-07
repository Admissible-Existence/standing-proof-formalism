# Standing Proof Whole-Repository Theory Map

## Canonical thesis

Standing is not inherited from prior review. A transition must reconstruct whether its actor, target, scope, policy, delegation, evidence, context, validity window, and recoverability still support standing at the consequence boundary.

```text
review evidence != execution authority
candidate record != standing proof
prior validity != current standing
```

## Source layers

| Layer | Canonical paths | Function |
|---|---|---|
| Thesis | `README.md`, `docs/STANDING_PROOF_STATUS.md` | Defines standing and non-authority boundaries. |
| Compact inputs | `data/standing-surfaces.json` | Enumerates the nine required standing surfaces. |
| Compact outputs | `data/standing-results.json` | Defines `ALLOW`, `DENY`, `FAIL_CLOSED`, and `INCOMPLETE`. |
| Integration status | `data/standing-integration.json` | Records linked domains without granting their authority. |
| Falsifiable cases | `data/standing-cases.json` | Exercises current-valid, stale, invalid, and incomplete standing. |
| Deterministic validation | `tools/check_standing_*.py` | Validates contracts and executable cases. |
| Organization completeness | `formalism/*`, `tools/validate_principle_completeness.py` | Indexes principles, dependencies, proof candidates, and evidence. |
| Coordination | `docs/STANDING_PROOF_FORMALISM_MIRROR_HANDOFF.md`, issue #1 | Preserves ownership, claims, evidence, and archive state. |

## Standing decision relation

Let the standing vector at boundary time `t_b` be:

```text
S(t_b) = (A, T, Sc, P, D, E, C, V, R)
```

where the components are actor, target, scope, policy, delegation, evidence, context, validity window, and recoverability.

The bounded repository rule is:

```text
ALLOW      iff every required component is explicitly VALID
DENY       iff every required component is present and at least one is INVALID
INCOMPLETE iff one or more required components are absent or UNKNOWN
FAIL_CLOSED for malformed/unrecognized inputs or validator failure
```

This relation produces a standing status record only. It does not execute a transition or convert standing into authority.

## Cross-repository boundary

Links to AE, BC, CHF, DC, DaCo, and StegVerse are dependency/context references only. This repository cannot inherit execution, publication, proof-acceptance, custody, or final-admissibility authority from them.
