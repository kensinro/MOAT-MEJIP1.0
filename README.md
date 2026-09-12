# AIDO-MOAT-MEJIP 1.0

**Evidence-bounded, auditable mechanism adjudication under partial observability for patient-level cancer molecular data.**

**Repository status:** `v1.0.0` — final public proof-layer release, 2026-09-12.  
**Purpose:** minimum executable reproducibility surface for the manuscript-facing MEJIP 1.0 adjudication logic.

MEJIP is designed for a problem that pathway scores or ranked candidate lists do not by themselves solve: **when does the available patient evidence actually entitle a mechanistic conclusion, and when must the result remain unresolved?**

This repository exposes a compact proof layer for inspecting those evidence-entitlement and adjudication behaviors without publishing private datasets, unpublished adapters, or post-MEJIP-1.0 experimental branches.

## What is included

- dependency-aware evidence collapse;
- explicit `SURVIVES`, `WEAK`, `FALSIFIED`, and `UNDERDETERMINED` states;
- decisive-contradiction retention;
- frozen MC1215 held-out RNA challenge rule;
- recovered Practical-1 Stage-11 ordered admission predicate;
- Practical-2 S9 ledger-integrity audit;
- simple same-task comparator baselines;
- machine-readable frozen-result registry with consistency checks;
- deterministic self-tests.

## Scientific interpretation

The executable surface is intentionally evidence-bounded:

- `MODEL_READY` = forward-model evaluability, **not** biological validation;
- `SURVIVES` = compatibility with qualified observed evidence under a frozen contract;
- `WEAK` = compatible but non-decisive evidence under the layer-specific contract;
- `FALSIFIED` = contradiction under a frozen challenge rule;
- `UNDERDETERMINED` = insufficient inferential entitlement, **not** computational failure.

The code does **not** establish causal truth, universal biological superiority, treatment utility, or a unique patient mechanism.

## Quick start

Requires Python 3.10 or later; the proof layer uses only the Python standard library.

```bash
python mejip_mvp.py self-test
python mejip_mvp.py frozen-registry
```

Optional frozen-ledger audit:

```bash
python mejip_mvp.py audit-p2-ledger P2_S9_MASTER_LEDGER.tsv
```

A successful self-test is an implementation-regression check. It is **not** biological or clinical validation.

## Reproducibility surface

`FROZEN_RESULT_REGISTRY.json` stores manuscript-scope verification counts and boundaries. `PACKAGE_MANIFEST_SHA256.json` records byte sizes and SHA256 values for the public package files.

No private patient-level data are bundled. No archival DOI is asserted in this repository unless and until a public archival service has actually minted and exposed one for the final `v1.0.0` release.

## MEJIP 1.0 scope boundary

The manuscript-facing MEJIP 1.0 scope is Practical 1–3, bounded Hallmark interpretation/robustness, E1 partial-observability robustness, and E2 Arm A.

The following are outside this public MEJIP 1.0 package: E2 Arm B signed-network hypotheses, E3, E4, E3-FD, C1, and cancer-attractor/state-transition work. E2 Arm B executed a real generator outside the formal MEJIP 1.0 S12 lineage, but **zero qualified external signed-network hypotheses entered formal generator-agnostic adjudication**.

## Citation

Citation metadata are provided in `CITATION.cff`. Cite the exact release/tag used. If an archival DOI is minted for `v1.0.0`, use the verified DOI from the archival record rather than a guessed or placeholder identifier.

## License

Released under the MIT License. See `LICENSE`.
