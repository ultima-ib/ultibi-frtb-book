# Performance

ultibi FRTB aggregator was built with performance in mind. Bellow table summarizes a large Equity portfolio:

```python
┌───────────┬──────────────┬────────────────┬───────────────┬──────────────┬─────────────────────┬─────────────────────┬─────────────────────────┐
│ RiskClass ┆ RiskCategory ┆ RiskFactorType ┆ TradeId_count ┆ PnL_Up_count ┆ BucketBCBS_n_unique ┆ RiskFactor_n_unique ┆ RiskFactorType_n_unique │
│ ---       ┆ ---          ┆ ---            ┆ ---           ┆ ---          ┆ ---                 ┆ ---                 ┆ ---                     │
│ str       ┆ str          ┆ str            ┆ u32           ┆ u32          ┆ u32                 ┆ u32                 ┆ u32                     │
╞═══════════╪══════════════╪════════════════╪═══════════════╪══════════════╪═════════════════════╪═════════════════════╪═════════════════════════╡
│ Equity    ┆ Delta        ┆ EqSpot         ┆ 648506        ┆ 648506       ┆ 4                   ┆ 18316               ┆ 1                       │
│ Equity    ┆ Delta        ┆ EqRepo         ┆ 219792        ┆ 219792       ┆ 3                   ┆ 18316               ┆ 1                       │
└───────────┴──────────────┴────────────────┴───────────────┴──────────────┴─────────────────────┴─────────────────────┴─────────────────────────┘
```

This portfolio consist of 868298 Equity Delta and Curvature (see PnL_Up_count) Sensitivities splic across 4 buckets, 18316 risk factors(equity names/tickers), with both Spot and Repo Present.

The result as of ultibi v0.1.3:
**--- Read DF time: 483.5027ms ---**
**--- Assign Weights time: 1.1574655s ---**

Just single EQ Delta Charge:

```python
request2 = dict(
    measures=[
        ["EQ DeltaCharge Medium", "scalar"]
    ],
    # Break down results by Group and BucketBCBS
    groupby=["Group"],

    # Show totals for each Group (note in this example only 1)
    totals = True,
    # Hide rows where each result is 0
    hide_zeros=True,
    calc_params={
        "jurisdiction": "BCBS",
        # Apply 21.98
        "apply_fx_curv_div": "true",
    },
)
```

**--- Compute time: 0.22789788246154785 seconds ---**

```python
request2 = dict(
    measures=[
        ["SBM Charge", "scalar"]
    ],
    # Break down results by Group and BucketBCBS
    groupby=["Group"],

    # Show totals for each Group (note in this example only 1)
    totals = True,
    # Hide rows where each result is 0
    hide_zeros=True,
    calc_params={
        "jurisdiction": "BCBS",
        # Apply 21.98
        "apply_fx_curv_div": "true",
    },
)
```

**--- Compute No Deps time: 2.538625478744507 seconds ---**

# Caching

Note, thanks to `ultibi's` internal caching mechanism, basic measures can be reused. For example:

```python
request = dict(
    measures=[
        ["SBM Charge High", "scalar"],
        ["SBM Charge Low", "scalar"],
        ["SBM Charge Medium", "scalar"]
    ],
    # Break down results by Group and BucketBCBS
    groupby=["Group"],

    # Show totals for each Group (note in this example only 1)
    totals = True,
    # Hide rows where each result is 0
    hide_zeros=True,
    calc_params={
        "jurisdiction": "BCBS",
        # Apply 21.98
        "apply_fx_curv_div": "true",
    },
)
```

**--- Compute No Deps time: 0.010367870330810547 seconds ---**

Compute time is almost identical to that of `request2`. This is because `SBM Charge` is a simple max of `SBM Charge Low`, `SBM Charge Medium`, `SBM Charge High` and therefore almost no additional compute is required.

**DataSet cache stores results of basic measures such as `EQ DeltaCharge Medium`. Therefore the next request will reuse them**.

# Standing on the shoulders of a giant: `Polars`

We use `Polars` in the backend, one of the fastest DataBase/DataFrame like ops solutions out there. Read more about the [benchmarks here](https://duckdblabs.github.io/db-benchmark/) to get a feel for how much data we can process and how fast. 
