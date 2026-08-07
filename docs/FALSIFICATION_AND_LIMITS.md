# Standing Proof Falsification and Limits

## Falsifiable claims

The current repository scope is falsified if any executable case or validated contract demonstrates one of the following:

1. **Inherited standing:** a transition receives `ALLOW` solely because an earlier review or earlier validity state was positive while the current validity window or context is invalid.
2. **Incomplete ALLOW:** any one of actor, target, scope, policy, delegation, evidence, context, validity window, or recoverability is `UNKNOWN` or absent and the result is `ALLOW`.
3. **Invalid-surface ALLOW:** every surface is present but at least one is `INVALID` and the result is `ALLOW`.
4. **Authority escalation:** a repository output changes `authority`, execution authorization, publication authorization, proof acceptance, custody, or final cross-repository validity from false to true.
5. **Silent schema acceptance:** malformed or unrecognized states are accepted without `FAIL_CLOSED` behavior at the validator boundary.

## Limits

This repository does not establish:

- universal legal standing;
- universal scientific correctness;
- physical execution authority;
- publication authority;
- proof acceptance authority;
- master-record custody;
- final cross-repository admissibility;
- truth of evidence merely because evidence is present;
- continuity merely because a standing record exists.

## Commit-time limit

A standing result is only about the evidence represented at the evaluated boundary. It must not be reused indefinitely as proof of future standing.

```text
prior validity != current standing
approval != continuity
execution != admissibility
```

## Failure posture

Malformed contracts, unknown state labels, validator exceptions, or unavailable required validation evidence must fail closed at the validation layer. Missing standing surfaces are reported as `INCOMPLETE` rather than silently promoted to `ALLOW`.
