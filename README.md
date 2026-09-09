<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright 2026 flxk1 -->
# loomground-collapse

**Which term took this conjunction to zero?**

Identifies the limiting term in a fail-closed conjunction.

## Install

```
pip install loomground-collapse
```

## Usage

```python
from loomground_collapse import Constituent, ConstituentState, collapse
out = collapse([Constituent("authority", ConstituentState.PRESENT),
                Constituent("timeliness", ConstituentState.AT_FLOOR)])
out.overall, out.issues
```

## Interface

- input: `Constituent(name, state, note)` · `ConstituentState`: `PRESENT` · `AT_FLOOR` · `UNASSIGNED`
- mapping `state_to_verdict`: `PRESENT → SATISFIED` · `AT_FLOOR → NOT_SATISFIED` · `UNASSIGNED → OPEN`
- output: `IssueAggregate(overall: Verdict, issues: (name, Verdict))`, weakest-link fold
- from solver: `cross_subsumption.Verdict` · `issue_aggregation.aggregate_issues`

## Family

Diagnostic operator; consumes `loomground-solver` 0.5; consumed by hosts. Pipeline: `source → loomground-ingest → loomground-versum → loomground-solver → loomground-collapse`. Operator contract: [spec/OPERATORS.md](https://github.com/flxk1/loomground/blob/main/spec/OPERATORS.md). [docs/operator.md](docs/operator.md).

## Status

0.1.0 · 14 tests · Python >=3.10 · solver 0.5

## License

Apache-2.0 `LICENSES/Apache-2.0.txt` (code) · CC-BY-4.0 `LICENSES/CC-BY-4.0.txt` (README) · `NOTICE`
