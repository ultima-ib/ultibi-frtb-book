import ultibi as ul

ds = ul.FRTBDataSet.from_config_path("./data/frtb/datasource_config.toml")

ds.measures
ul.aggregation_ops()

# What do we want to calculate?
request = dict(
    measures=[
        ["DRC nonSec GrossJTD", "sum"],
        ["DRC nonSec GrossJTD Scaled", "sum"],
        ["DRC nonSec CapitalCharge", "scalar"],
        ["DRC nonSec NetLongJTD", "scalar"],
        ["DRC nonSec NetShortJTD", "scalar"],
        ["DRC nonSec NetLongJTD Weighted", "scalar"],
        ["DRC nonSec NetAbsShortJTD Weighted", "scalar"],
        ["DRC nonSec HBR", "scalar"],
    ],
    groupby=["Desk", "BucketBCBS"],
    hide_zeros=True,
    calc_params={
        "jurisdiction": "BCBS",
        "apply_fx_curv_div": "true",
        "drc_offset": "true",
    },
)

aggrequest = ul.AggRequest(request)

result = ds.compute(request)
# print(result)
# print("Type: ", type(result))
