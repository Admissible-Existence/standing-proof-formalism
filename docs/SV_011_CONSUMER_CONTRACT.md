# SV-011 Standing Consumer Contract

Status: PREPARED_EXTERNAL_DEPENDENCY
Updated: 2026-09-01
Consumer: `SV-011/entity`
Authority effect: NONE

## Required standing semantics

SV-011 may consume this repository only to reconstruct current standing at a consequence boundary.

The consumer must preserve:

- review evidence != execution authority
- candidate record != standing proof
- prior validity != current standing
- ALLOW standing status != execution permission

For each required surface, current validity must be explicit. Missing required surfaces remain incomplete/fail-closed; invalid surfaces cannot silently produce ALLOW; stale evidence cannot inherit current standing.

## Construction use

During SV-011 Phase 1, every claimed principle/capability candidate must name:
- required standing surfaces,
- a falsification condition,
- freshness requirements,
- the consumer-side receipt that records the evaluated result.

## Non-transfer

This contract does not issue standing to SV-011 and grants no execution, publication, proof-acceptance, custody, runtime, or release authority.
