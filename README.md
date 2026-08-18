<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright 2026 flxk1 -->
# loomground-collapse

**Which term took this conjunction to zero?**

Weakest-link over a decomposition where any term at its floor collapses the whole. No product, no score, and a measured floor stays distinct from an unmeasured term.

## Scope

One problem. This package answers the question above and nothing adjacent to it.
If a change here would also need a second question answered, it belongs in a
different repository.

## Where it sits

```
grammar ──▶ versum ──▶ solver ──▶ loomground-collapse
```

Above the reasoning kernel, never beside it. It uses `loomground-solver`'s shared
three-valued verdict, its OPEN-dominant strict-AND fold, and its injected ports —
and reaches into no solver internals. Nothing in the kernel imports this package,
and nothing here imports governance, a corpus, or a domain.

## Contract

The package **reports**; it resolves nothing and decides nothing. Judgements
arrive already made, from whoever can be held to them, and are compared rather
than derived. Where a term is absent it escalates rather than passing: an
unmeasured input is not the same as a satisfied one, and the two never collapse
into a single value.

## Install

```
pip install loomground-collapse
```

## Licence

Apache-2.0 for the code; CC-BY-4.0 for the prose in this README. See `NOTICE`.
