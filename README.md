# Skill Constellation

### Observation note: a claim is not a credential

A subject names a narrowly bounded skill, two pre-approved assessor wallets, one public rubric, and a validity period. Nothing becomes active at creation.

### Observation note: two independent orbits

Each assessor may contribute exactly once and must use a fresh evidence origin. Validators retrieve the common rubric and the assessor artifact, then independently agree on a supported integer level from 0 through 5. The active level is the lower of the two results, not an optimistic average.

### Observation note: stars expire

`CLAIMED → ASSESSED → ACTIVE → EXPIRED / REVOKED`

Expiry is permissionless. Revocation is limited to the named assessors and requires a new evidence origin. Every artifact and digest stays attributable.

```bash
genvm-lint contracts/contract.py
python -m pytest -q
```

The public interface is a navigable constellation, deliberately unrelated to Trust Repair's kintsugi ledger. Deployment coordinates are recorded only after a finalized live assessment.
