import ultibi as ul
import polars as pl

pl.Config.set_tbl_rows(100)
ds = ul.FRTBDataSet.from_config_path("./data/frtb/datasource_config.toml")


request = dict(
    measures=[["SBM Charge", "scalar"]],
    groupby=["Country", "RiskClass"],
    filters=[[{"op": "Eq", "field": "Desk", "value": "FXOptions"}]],
    hide_zeros=True,
    totals=True,
    calc_params={
        "jurisdiction": "BCBS",
        "apply_fx_curv_div": "true",
        "drc_offset": "true",
    },
)
result = ds.compute(request)

request = dict(
    measures=[["SBM Charge", "scalar"]],
    groupby=["Country", "RiskClass"],
    filters=[[{"op": "Neq", "field": "Desk", "value": "FXOptions"}]],
    hide_zeros=True,
    totals=True,
    calc_params={
        "jurisdiction": "BCBS",
        "apply_fx_curv_div": "true",
        "drc_offset": "true",
    },
)
result = ds.compute(request)

request = dict(
    measures=[["SBM Charge", "scalar"]],
    groupby=["Country", "RiskClass"],
    filters=[[{"op": "In", "field": "Desk", "value": ["FXOptions", "Rates"]}]],
    hide_zeros=True,
    totals=True,
    calc_params={
        "jurisdiction": "BCBS",
        "apply_fx_curv_div": "true",
        "drc_offset": "true",
    },
)
result = ds.compute(request)

request = dict(
    measures=[["SBM Charge", "scalar"]],
    groupby=["Country", "RiskClass"],
    filters=[[{"op": "NotIn", "field": "Desk", "value": ["FXOptions", "Rates"]}]],
    hide_zeros=True,
    totals=True,
    calc_params={
        "jurisdiction": "BCBS",
        "apply_fx_curv_div": "true",
        "drc_offset": "true",
    },
)
result = ds.compute(request)

request = dict(
    measures=[["SBM Charge", "scalar"]],
    groupby=["Country", "RiskClass"],
    filters=[
        [
            {"op": "Eq", "field": "LegalEntity", "value": "EMEA"},
            {"op": "Eq", "field": "Country", "value": "UK"},
        ],
        [{"op": "In", "field": "RiskClass", "value": ["FX", "Equity"]}],
    ],
    hide_zeros=True,
    totals=True,
    calc_params={
        "jurisdiction": "BCBS",
        "apply_fx_curv_div": "true",
        "drc_offset": "true",
    },
)
result = ds.compute(request)
