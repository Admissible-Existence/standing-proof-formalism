# Standing Proof Mathematical Notation

Let the consequence boundary time be `t_b`.

Define the standing vector:

```text
S(t_b) = (A, T, Sc, P, D, E, C, V, R)
```

with:

- `A` actor standing surface;
- `T` target standing surface;
- `Sc` scope surface;
- `P` policy surface;
- `D` delegation surface;
- `E` evidence surface;
- `C` context surface;
- `V` validity-window surface;
- `R` recoverability surface.

Each required component has one bounded state:

```text
VALID, INVALID, UNKNOWN
```

For a complete vector:

```text
ALLOW(S) iff forall s in S: s = VALID
DENY(S) iff (forall s in S: s != UNKNOWN) and (exists s in S: s = INVALID)
INCOMPLETE(S) iff exists s in S: s = UNKNOWN
```

Malformed inputs, unrecognized states, validator failures, or missing required contracts produce `FAIL_CLOSED` at the validation boundary.

## Time dependence

Current standing is evaluated at `t_b`:

```text
Standing(t_prior) does not imply Standing(t_b)
```

In particular:

```text
V(t_b) = INVALID => ALLOW is impossible
C(t_b) = INVALID => ALLOW is impossible
D(t_b) = INVALID => ALLOW is impossible
```

The repository does not define `ALLOW` as execution permission. It is only the result class of the standing-status formalism.
