# Standing Proof Formalism

## Status

Early formalism repository for the `Admissible-Existence` organization.

This repository defines **Standing Proof Formalism**: the review layer for determining whether an actor, system, transition, authority basis, evidence set, and context still have standing at the relevant boundary.

## Core Thesis

Standing is not inherited from prior review.

Standing must be determined at the boundary where consequence may be committed.

```text
review evidence != execution authority
candidate record != standing proof
prior validity != current standing
```

## Purpose

Standing Proof Formalism exists to prevent stale, substituted, incomplete, or context-invalid evidence from becoming authority by default.

A standing proof asks whether the current actor, target, scope, policy, delegation, evidence, context, validity window, and recoverability state still support the transition being considered.

## Minimum Standing Surfaces

```text
actor_surface
target_surface
scope_surface
policy_surface
delegation_surface
evidence_surface
context_surface
validity_window_surface
recoverability_surface
```

## Result Classes

```text
ALLOW
DENY
FAIL_CLOSED
INCOMPLETE
```

## Relationship to AE

AE asks whether existence remains admissible across transition.

Standing Proof asks whether the current proof basis is sufficient to evaluate or commit a specific transition.

## Relationship to StegVerse

Standing Proof maps to StegVerse commit-time admissibility and execution authority review.

The formalism is status-record only in this repository. It does not grant authority, execute transitions, or claim cross-repo validity.
