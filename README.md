# Ultima's Python FRTB SA Aggregator 

[This](https://ultimabi.uk/frtb-book/) is a free python binding to implementation of Fundamental Review of the Trading Book (FRTB SA). Supports multiple jurisdictions (BCBS, CRR2). Aggregates at any level of breakdown. Supports everything you'd need in a proper production environment: Filtering, Overrides and WhatIf. Blazingly fast, leveraging on Rust and [polars](https://pola-rs.github.io/polars-book/user-guide/).

Currently covering SA (Standardised Approach), with some limitations, it will be extended to cover IMA (Internal Models Approach) and SA CVA shortly. Checkout our [userguide](https://ultimabi.uk/frtb-book/). 

 ## Get started
 `pip install ultibi`

## Acknowledgements
[Ultima](https://ultimabi.uk/).

## Contributing

You will need `python`, `make`, `wget` and [`mdbook`](https://github.com/rust-lang/mdBook/releases).

### Before commit

*All examples must be plased into src/examples and refered to from .md files as `{#include ./examples/...}`*


While developing:
`mdbook watch --open`

Download data:
`make data`

Build venv:
`make venv`

Linting:
`make fmt`

Tests\\examples:
`make run`
