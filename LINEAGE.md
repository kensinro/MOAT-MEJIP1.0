# Lineage and immutability

The final `v1.0.0` public proof-layer release is derived from `v1.0.0-rc.2` after manuscript–SI regression, final substantive audit, Final Human Gate, post-Human delta regression, and L0 Final Lock.

The RC2 code/result surface was verified before final release staging: `main` and tag `v1.0.0-rc.2` both pointed to commit `c60bfcee5a945ad09ca6d6fd1cb5be3aae9006cd`, with no post-RC2 code drift detected.

The final-release staging changes only release metadata (`CITATION.cff`, `README.md`, `LINEAGE.md`, and `PACKAGE_MANIFEST_SHA256.json`). It does not alter executable adjudication logic, frozen experimental results, denominators, terminal states, evidence roles, or claim ceilings.

Rule: **copy, isolate, subtitle, trace — never rewrite the frozen scientific parent in place.**
