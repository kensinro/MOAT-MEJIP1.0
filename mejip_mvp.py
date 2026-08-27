#!/usr/bin/env python3
"""
AIDO-MOAT-MEJIP — Public Proof Layer / Minimum Reproducibility MVP
==================================================================

Version: 1.0.1-public-mvp-rc-2026-08-28

This public file intentionally exposes only the smallest executable core needed to
inspect the paper-facing mechanism-evidence adjudication behavior:

- typed evidence-jigsaw rows;
- dependency-group collapse;
- explicit abstention/uncertainty;
- decisive contradiction preservation;
- frozen MC1215 held-out challenge rule;
- simple comparator baselines;
- recovered Stage-11 forward-model admission predicate;
- frozen P2-S9 ledger integrity checks;
- manuscript-scope frozen-result registry audit;
- deterministic self-tests.

MEJIP 1.0 scope note:
- Practical 1-3 + bounded Hallmark + E1 + E2 Arm A are manuscript-facing.
- E2 Arm B, E3, E4, E3-FD, and C1 are not part of this MEJIP 1.0 public MVP.

Not included:
- private/internal orchestration;
- recovery automation;
- unpublished generator adapters;
- future optimization/AI routing;
- unexecuted external comparator integrations;
- private data or resource payloads.

This code does not provide treatment recommendations and does not claim that synthetic
benchmark conformance is biological or causal accuracy.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence


VERSION = "1.0.1-public-mvp-rc-2026-08-28"

P2_S9_MASTER_LEDGER_SHA256 = "9b70f68f3f21c99440958b2780c270a025d49600d25316cbaf4081838194c093"

P2_EXPECTED = {
    "rows": 18649,
    "patients": 1097,
    "candidates": 17,
    "terminal_counts": {
        "SURVIVES": 285,
        "WEAK": 12699,
        "FALSIFIED": 686,
        "UNDERDETERMINED": 4979,
    },
    "mc1215_counts": {
        "SURVIVES": 285,
        "WEAK": 21,
        "FALSIFIED": 686,
        "UNDERDETERMINED": 105,
    },
}

MC1215_HOLDOUT_GENES = ("CDKN1A","GADD45A","SFN","CDC25C")
MC1215_DECISIVE_GENES = frozenset({"CDKN1A","CDC25C"})
MC1215_GAIN_EXPECTATION = {
    "CDKN1A": 1,
    "GADD45A": 1,
    "SFN": 1,
    "CDC25C": -1,
}


STAGE11_EXPECTED = {
    "candidate_family": 1307,
    "NO_TOPOLOGY": 163,
    "NO_SIGNED_EDGE": 33,
    "NO_BP_LINKED_SIGNED_ANCHOR": 81,
    "NO_RESOLVED_NONSEED_NEIGHBORHOOD": 274,
    "MODEL_READY": 756,
}

FROZEN_RESULT_REGISTRY = {'release_identity': 'MEJIP-1.0-manuscript-scope-locked-2026-08-28', 'scope': {'included': ['Practical 1', 'Practical 2', 'Practical 3', 'bounded Hallmark', 'E1 observability robustness', 'E2 Arm A GSVA native-task comparator'], 'excluded_from_mejip1': ['E2 Arm B signed-network hypotheses', 'E3', 'E4', 'E3-FD', 'C1', 'cancer-attractor/state-transition work'], 'boundary': 'frozen results are evidence states and audit results, not causal truth or treatment recommendations'}, 'stage11': {'candidate_family': 1307, 'no_topology': 163, 'no_signed_edge': 33, 'no_bp_linked_signed_anchor': 81, 'no_resolved_nonseed_neighborhood': 274, 'model_ready': 756, 'replay_mismatches': 0, 'candidate_set_sha256': 'b1d5bc24dc939771494d92116ccfe8cd5bbae566bab62e076ee528f974a22202'}, 'locked_metabric_transfer': {'denominator': 756, 'SURVIVES': 17, 'WEAK': 61, 'FALSIFIED': 29, 'UNDERDETERMINED': 649}, 'cross_cancer_append_only': {'candidates': 17, 'non_brca_cohorts': 17, 'tests': 289, 'global_fdr_pairs': 11, 'same_direction': 10, 'opposite_direction': 1, 'candidates_with_ge1_same_direction': 7, 'candidates_with_ge2_same_direction': 3, 'candidates_with_no_global_fdr_signal': 9}, 'patient_adjudication': {'patients': 1097, 'candidates': 17, 'rows': 18649, 'SURVIVES': 285, 'WEAK': 12699, 'FALSIFIED': 686, 'UNDERDETERMINED': 4979, 'full_space_identifiable_patients': 0, 'mc1215': {'SURVIVES': 285, 'WEAK': 21, 'FALSIFIED': 686, 'UNDERDETERMINED': 105, 'PROCESS_GAIN': 483, 'PROCESS_LOSS': 509, 'NON_IDENTIFIABLE': 105}}, 'practical3_controlled_stress': {'challenge_families': 8, 'cases_per_family': 8, 'cases': 64, 'methods': 4, 'native_outputs': 256, 'abstention_fidelity': '40/40', 'decisive_falsifier_retention': '16/16', 'contradiction_visibility': '40/40', 'dependency_decision_change_rate': '0/8', 'order_invariance': '24/24', 'unsupported_positivity': '0/16', 'adversarial_reproduction': '24/24'}, 'hallmark_append_only': {'candidate_hallmark_tests_per_representation': 850, 'primary_supported_mappings': 40, 'primary_candidates_mapped': 9, 'primary_hallmarks_mapped': 23, 'full_reactome_sensitivity_mappings': 59, 'descriptive_programs': 9, 'degree_null_mean': 9.14, 'degree_null_upper_tail_p': 0.768}, 'e1_observability': {'upward_entitlement_violations': 0, 'upward_entitlement_denominator': 91, 'ceiling_violations': 0, 'ceiling_denominator': 51, 'random_single_object_downgrades': 1086, 'random_single_object_masks': 4000, 'supportive_structured_downgrade_rate': 0.0, 'source_essential_primary_downgrade_rate': 1.0, 'role_permutation_global_empirical_p': 0.497, 'kegg_source_essential_response': '6/10', 'tcga_projection_rows': 4388, 'tcga_projection_full_state_eligible': 0}, 'e2_arm_a_gsva': {'hallmarks': 50, 'primary_nominations': 0, 'bootstrap_repeats': 1000, 'bootstrap_direction_consistency_threshold': 0.95, 'subsamples': 500, 'subsample_fraction': 0.8, 'recurrence_threshold': 0.8, 'interpretation': 'valid native-task null; no cross-task superiority'}, 'e2_arm_b_boundary': {'status': 'FINAL_CLOSED_OUTSIDE_MEJIP1_FORMAL_S12', 'generator_execution_occurred': True, 'formal_s12_admitted_hypotheses': 0, 'solver_limit_seconds': 3600, 'reported_gap': 0.12, 'target_gap': 0.0001, 'wording_rule': 'Do not state that signed causal-network generation never occurred; state that no qualified external signed-network hypothesis entered formal generator-agnostic adjudication in the reported MEJIP 1.0 empirical scope.'}, 'tcga_reuse_boundary': {'discovery_cohort': 'TCGA-BRCA', 'patient_adjudication_cohort': 'TCGA-BRCA', 'independent_patient_level_replication': False, 'guardrail': 'Candidate membership was locked through METABRIC before patient-level adjudication, but the TCGA patient-state distribution is not an independent patient-level replication.'}}

def stage11_admission(
    topology_supported: bool,
    signed_edges_n: int,
    eligible_seed_nodes_n: int,
    propagated_resolved_nodes_n: int,
) -> str:
    """Recovered ordered Stage-11 admission predicate.

    This is an evaluability predicate, not a biological-validation rank.
    Precedence is fixed and must not be reordered post hoc.
    """
    if not bool(topology_supported):
        return "NO_TOPOLOGY"
    if int(signed_edges_n) <= 0:
        return "NO_SIGNED_EDGE"
    if int(eligible_seed_nodes_n) <= 0:
        return "NO_BP_LINKED_SIGNED_ANCHOR"
    if int(propagated_resolved_nodes_n) <= 0:
        return "NO_RESOLVED_NONSEED_NEIGHBORHOOD"
    return "MODEL_READY"

def validate_frozen_registry() -> dict[str, Any]:
    r = FROZEN_RESULT_REGISTRY
    checks = {}
    s11 = r["stage11"]
    checks["stage11_partition"] = (s11["no_topology"] + s11["no_signed_edge"] + s11["no_bp_linked_signed_anchor"] + s11["no_resolved_nonseed_neighborhood"] + s11["model_ready"] == s11["candidate_family"])
    mt = r["locked_metabric_transfer"]
    checks["metabric_partition"] = sum(mt[k] for k in ("SURVIVES","WEAK","FALSIFIED","UNDERDETERMINED")) == mt["denominator"]
    p2 = r["patient_adjudication"]
    checks["patient_rows"] = p2["rows"] == p2["patients"] * p2["candidates"]
    checks["patient_partition"] = sum(p2[k] for k in ("SURVIVES","WEAK","FALSIFIED","UNDERDETERMINED")) == p2["rows"]
    p3 = r["practical3_controlled_stress"]
    checks["stress_outputs"] = p3["native_outputs"] == p3["cases"] * p3["methods"]
    h = r["hallmark_append_only"]
    checks["hallmark_denominator"] = h["candidate_hallmark_tests_per_representation"] == 17 * 50
    e2 = r["e2_arm_a_gsva"]
    checks["gsva_null_in_bounds"] = 0 <= e2["primary_nominations"] <= e2["hallmarks"]
    checks["e2b_not_in_s12"] = r["e2_arm_b_boundary"]["formal_s12_admitted_hypotheses"] == 0
    return {"pass": all(checks.values()), "checks": checks}


class Polarity(str, Enum):
    SUPPORT = "SUPPORT"
    CONTRADICT = "CONTRADICT"
    UNAVAILABLE = "UNAVAILABLE"


class TerminalState(str, Enum):
    SURVIVES = "SURVIVES"
    WEAK = "WEAK"
    FALSIFIED = "FALSIFIED"
    UNDERDETERMINED = "UNDERDETERMINED"


class Direction(str, Enum):
    PROCESS_GAIN = "PROCESS_GAIN"
    PROCESS_LOSS = "PROCESS_LOSS"
    NON_IDENTIFIABLE = "NON_IDENTIFIABLE"


@dataclass(frozen=True)
class EvidenceItem:
    evidence_id: str
    dependency_group: str
    polarity: Polarity
    observed: bool = True
    decisive: bool = False
    provenance_token: str = ""

    def usable(self) -> bool:
        return self.observed and self.polarity != Polarity.UNAVAILABLE


def sha256_file(path: str | Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def dependency_states(items: Sequence[EvidenceItem]) -> dict[str, str]:
    """
    Collapse same-dependency rows so duplicates do not become independent evidence.
    """
    groups: dict[str, list[EvidenceItem]] = defaultdict(list)
    for x in items:
        groups[x.dependency_group].append(x)

    out = {}
    for g, rows in groups.items():
        sup = any(x.usable() and x.polarity == Polarity.SUPPORT for x in rows)
        con = any(x.usable() and x.polarity == Polarity.CONTRADICT for x in rows)
        dec = any(
            x.usable() and x.polarity == Polarity.CONTRADICT and x.decisive
            for x in rows
        )
        if dec:
            out[g] = "DECISIVE_CONTRADICTION"
        elif sup and con:
            out[g] = "CONFLICT"
        elif sup:
            out[g] = "SUPPORT"
        elif con:
            out[g] = "CONTRADICT"
        else:
            out[g] = "UNAVAILABLE"
    return out


def mejip_behavioral_adjudication(items: Sequence[EvidenceItem]) -> dict[str, Any]:
    """
    Public behavioral kernel used for paper-facing controlled tests.

    This is not a replacement for candidate-specific biological rules.
    """
    states = dependency_states(items)
    decisive = any(x == "DECISIVE_CONTRADICTION" for x in states.values())
    support = sum(x == "SUPPORT" for x in states.values())
    contradict = sum(x in {"CONTRADICT","DECISIVE_CONTRADICTION","CONFLICT"} for x in states.values())

    if decisive:
        terminal = TerminalState.FALSIFIED
    elif not states or all(x == "UNAVAILABLE" for x in states.values()):
        terminal = TerminalState.UNDERDETERMINED
    elif any(x == "CONFLICT" for x in states.values()):
        terminal = TerminalState.UNDERDETERMINED
    elif support > 0 and contradict == 0:
        terminal = TerminalState.SURVIVES
    elif contradict > 0 and support == 0:
        terminal = TerminalState.WEAK
    else:
        terminal = TerminalState.UNDERDETERMINED

    return {
        "terminal_state": terminal.value,
        "effective_support_groups": support,
        "effective_contradiction_groups": contradict,
        "decisive_contradiction": decisive,
        "contradiction_visible": contradict > 0,
        "provenance_tokens": sorted(
            {x.provenance_token for x in items if x.provenance_token}
        ),
    }


def _expected_sign(gain_sign: int, direction: Direction) -> int:
    if direction == Direction.PROCESS_GAIN:
        return gain_sign
    if direction == Direction.PROCESS_LOSS:
        return -gain_sign
    raise ValueError("NON_IDENTIFIABLE has no expected sign")


def mc1215_holdout(
    direction: Direction,
    observed_signs: Mapping[str, int | float | None],
) -> dict[str, Any]:
    """
    Frozen Practical-2 MC1215 held-out RNA challenge.

    FALSIFIED:
      contradictions >= 2 and at least one is CDKN1A or CDC25C

    SURVIVES:
      at least 3 of 4 matches and no decisive contradiction

    WEAK:
      residual identifiable state

    UNDERDETERMINED:
      24-node direction was NON_IDENTIFIABLE
    """
    if direction == Direction.NON_IDENTIFIABLE:
        return {
            "terminal_state": TerminalState.UNDERDETERMINED.value,
            "matches": [],
            "contradictions": [],
            "missing": list(MC1215_HOLDOUT_GENES),
            "decisive_contradiction": False,
        }

    matches, contradictions, missing = [], [], []
    for gene in MC1215_HOLDOUT_GENES:
        value = observed_signs.get(gene)
        if value is None:
            missing.append(gene)
            continue
        try:
            value = float(value)
        except Exception:
            missing.append(gene)
            continue
        if not math.isfinite(value) or value == 0:
            missing.append(gene)
            continue
        obs = 1 if value > 0 else -1
        exp = _expected_sign(MC1215_GAIN_EXPECTATION[gene], direction)
        (matches if obs == exp else contradictions).append(gene)

    decisive = (
        len(contradictions) >= 2
        and bool(MC1215_DECISIVE_GENES.intersection(contradictions))
    )

    if decisive:
        state = TerminalState.FALSIFIED
    elif len(matches) >= 3:
        state = TerminalState.SURVIVES
    else:
        state = TerminalState.WEAK

    return {
        "terminal_state": state.value,
        "matches": matches,
        "contradictions": contradictions,
        "missing": missing,
        "decisive_contradiction": decisive,
    }


def naive_union(items: Sequence[EvidenceItem]) -> dict[str, Any]:
    obs = [x for x in items if x.usable()]
    retained = any(x.polarity == Polarity.SUPPORT for x in obs)
    return {"native_state":"RETAINED" if retained else "NOT_RETAINED"}


def equal_voting(items: Sequence[EvidenceItem]) -> dict[str, Any]:
    obs = [x for x in items if x.usable()]
    sup = sum(x.polarity == Polarity.SUPPORT for x in obs)
    con = sum(x.polarity == Polarity.CONTRADICT for x in obs)
    score = sup - con
    if not obs:
        state = "NO_EVIDENCE"
    elif score > 0:
        state = "POSITIVE"
    elif score < 0:
        state = "NEGATIVE"
    else:
        state = "TIE"
    return {"native_state":state,"score":score}


def simple_counting(items: Sequence[EvidenceItem]) -> dict[str, Any]:
    obs = [x for x in items if x.usable()]
    sup = sum(x.polarity == Polarity.SUPPORT for x in obs)
    con = sum(x.polarity == Polarity.CONTRADICT for x in obs)
    if sup > con:
        state = "POSITIVE"
    elif con > sup:
        state = "NEGATIVE"
    else:
        state = "TIE"
    return {
        "native_state":state,
        "support":sup,
        "contradiction":con,
        "unavailable":len(items)-len(obs),
    }


def audit_p2_s9_ledger(path: str | Path, require_frozen_hash: bool = False) -> dict[str, Any]:
    p = Path(path)
    observed_sha = sha256_file(p)
    if require_frozen_hash and observed_sha != P2_S9_MASTER_LEDGER_SHA256:
        return {
            "pass":False,
            "reason":"SHA256_MISMATCH",
            "expected":P2_S9_MASTER_LEDGER_SHA256,
            "observed":observed_sha,
        }

    with p.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        rows = list(reader)
        fields = reader.fieldnames or []

    def col(*aliases):
        lut = {x.lower():x for x in fields}
        return next((lut[a.lower()] for a in aliases if a.lower() in lut), None)

    pc = col("patient_id","patient","sample_id","case_id","submitter_id")
    cc = col("candidate_id","candidate","mechanism_id")
    sc = col("terminal_state","state","adjudication_state")
    if not (pc and cc and sc):
        return {"pass":False,"reason":"REQUIRED_COLUMNS_NOT_FOUND","fields":fields}

    patients = {r[pc] for r in rows}
    candidates = {r[cc] for r in rows}
    states = Counter(r[sc] for r in rows)
    mc = Counter(r[sc] for r in rows if r[cc] == "MC1215")
    pairs = {(r[pc],r[cc]) for r in rows}
    per_patient = Counter(r[pc] for r in rows)

    checks = {
        "rows":len(rows) == P2_EXPECTED["rows"],
        "patients":len(patients) == P2_EXPECTED["patients"],
        "candidates":len(candidates) == P2_EXPECTED["candidates"],
        "unique_pairs":len(pairs) == len(rows),
        "17_rows_per_patient":bool(per_patient) and set(per_patient.values()) == {17},
        "terminal_counts":all(states[k] == v for k,v in P2_EXPECTED["terminal_counts"].items()),
        "mc1215_counts":all(mc[k] == v for k,v in P2_EXPECTED["mc1215_counts"].items()),
    }
    return {
        "pass":all(checks.values()),
        "sha256":observed_sha,
        "exact_frozen_hash":observed_sha == P2_S9_MASTER_LEDGER_SHA256,
        "checks":checks,
        "observed":{
            "rows":len(rows),
            "patients":len(patients),
            "candidates":len(candidates),
            "terminal_counts":dict(states),
            "mc1215_counts":dict(mc),
        },
    }


def self_test() -> dict[str, Any]:
    def item(eid, pol, group, decisive=False, observed=True):
        return EvidenceItem(
            evidence_id=eid,
            dependency_group=group,
            polarity=pol,
            observed=observed,
            decisive=decisive,
            provenance_token=f"PROV:{eid}",
        )

    tests = {}
    duplicated = [
        item("s1",Polarity.SUPPORT,"G1"),
        item("s2",Polarity.SUPPORT,"G1"),
        item("c",Polarity.CONTRADICT,"G2"),
    ]
    tests["dependency_collapse"] = len(dependency_states(duplicated)) == 2

    decisive = [
        item("s",Polarity.SUPPORT,"G1"),
        item("c",Polarity.CONTRADICT,"G2",decisive=True),
    ]
    tests["decisive_falsifier"] = (
        mejip_behavioral_adjudication(decisive)["terminal_state"] == "FALSIFIED"
    )

    s = mc1215_holdout(
        Direction.PROCESS_GAIN,
        {"CDKN1A":1,"GADD45A":1,"SFN":1,"CDC25C":-1},
    )
    tests["mc1215_survives"] = s["terminal_state"] == "SURVIVES"

    f = mc1215_holdout(
        Direction.PROCESS_GAIN,
        {"CDKN1A":-1,"GADD45A":1,"SFN":1,"CDC25C":1},
    )
    tests["mc1215_falsified"] = f["terminal_state"] == "FALSIFIED"

    u = mc1215_holdout(Direction.NON_IDENTIFIABLE,{})
    tests["mc1215_abstains_on_direction_tie"] = u["terminal_state"] == "UNDERDETERMINED"

    conflict = [
        item("s",Polarity.SUPPORT,"G1"),
        item("c",Polarity.CONTRADICT,"G2"),
    ]
    tests["equal_vote_tie"] = equal_voting(conflict)["native_state"] == "TIE"
    tests["simple_count_tie"] = simple_counting(conflict)["native_state"] == "TIE"
    tests["naive_union_retains"] = naive_union(conflict)["native_state"] == "RETAINED"
    tests["stage11_no_topology"] = stage11_admission(False, 5, 2, 3) == "NO_TOPOLOGY"
    tests["stage11_no_signed"] = stage11_admission(True, 0, 2, 3) == "NO_SIGNED_EDGE"
    tests["stage11_no_anchor"] = stage11_admission(True, 5, 0, 3) == "NO_BP_LINKED_SIGNED_ANCHOR"
    tests["stage11_no_neighborhood"] = stage11_admission(True, 5, 2, 0) == "NO_RESOLVED_NONSEED_NEIGHBORHOOD"
    tests["stage11_model_ready"] = stage11_admission(True, 5, 2, 3) == "MODEL_READY"
    tests["frozen_registry"] = validate_frozen_registry()["pass"]

    return {"version":VERSION,"pass":all(tests.values()),"tests":tests}


def cli() -> int:
    p = argparse.ArgumentParser(prog="mejip", description=__doc__)
    sp = p.add_subparsers(dest="cmd", required=True)

    sp.add_parser("self-test")
    sp.add_parser("frozen-registry", help="Print and validate manuscript-scope frozen result registry")

    h = sp.add_parser("hash")
    h.add_argument("path")

    a = sp.add_parser("audit-p2-ledger")
    a.add_argument("path")
    a.add_argument("--require-frozen-hash", action="store_true")

    m = sp.add_parser("mc1215")
    m.add_argument("--direction", choices=[x.value for x in Direction], required=True)
    for gene in MC1215_HOLDOUT_GENES:
        m.add_argument(f"--{gene}", type=float, default=None)

    args = p.parse_args()
    if args.cmd == "self-test":
        r = self_test()
        print(json.dumps(r, indent=2))
        return 0 if r["pass"] else 2
    if args.cmd == "frozen-registry":
        out = {"version": VERSION, "validation": validate_frozen_registry(), "registry": FROZEN_RESULT_REGISTRY}
        print(json.dumps(out, indent=2))
        return 0 if out["validation"]["pass"] else 4
    if args.cmd == "hash":
        print(sha256_file(args.path))
        return 0
    if args.cmd == "audit-p2-ledger":
        r = audit_p2_s9_ledger(args.path, args.require_frozen_hash)
        print(json.dumps(r, indent=2))
        return 0 if r["pass"] else 3
    if args.cmd == "mc1215":
        signs = {g:getattr(args,g) for g in MC1215_HOLDOUT_GENES}
        print(json.dumps(mc1215_holdout(Direction(args.direction), signs), indent=2))
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(cli())
