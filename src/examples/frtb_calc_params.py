import ultibi as ul
import json

ds = ul.FRTBDataSet.from_config_path("./data/frtb/datasource_config.toml")

for calc_param in ds.calc_params:
    if "com_delta_" in calc_param[0]:
        # print(calc_param) #<-- uncomment to see
        pass
# fmt: off
com_delta_diff_cty_rho_per_bucket_base = json.dumps(
    [1.55, 1.95, 1.4, 1.8, 1.6, 1.65, 1.55, 1.45, 1.15, 1.4, 1.15]
)
com_delta_gamma_low = json.dumps(
    {
        "v": 1,
        "dim": [11, 11],
        "data": [
            0.0,1.2,1.2,1.2,1.2,1.2,1.2,1.2,1.2,1.2,0.0,
            1.2,0.0,1.2,1.2,1.2,1.2,1.2,1.2,1.2,1.2,0.0,
            1.2,1.2,0.0,1.2,1.2,1.2,1.2,1.2,1.2,1.2,0.0,
            1.2,1.2,1.2,0.0,1.2,1.2,1.2,1.2,1.2,1.2,0.0,
            1.2,1.2,1.2,1.2,0.0,1.2,1.2,1.2,1.2,1.2,0.0,
            1.2,1.2,1.2,1.2,1.2,0.0,1.2,1.2,1.2,1.2,0.0,
            1.2,1.2,1.2,1.2,1.2,1.2,0.0,1.2,1.2,1.2,0.0,
            1.2,1.2,1.2,1.2,1.2,1.2,1.2,0.0,1.2,1.2,0.0,
            1.2,1.2,1.2,1.2,1.2,1.2,1.2,1.2,0.0,1.2,0.0,
            1.2,1.2,1.2,1.2,1.2,1.2,1.2,1.2,1.2,0.0,0.0,
            0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
        ],
    }
)
# fmt: on
calc_params = dict(
    com_delta_diff_cty_rho_per_bucket_base=com_delta_diff_cty_rho_per_bucket_base,
    com_delta_gamma_low=com_delta_gamma_low,
)
print(calc_params)

request1 = dict(
    measures=[
        ["Commodity DeltaCharge Low", "scalar"],
        ["Commodity DeltaCharge Medium", "scalar"],
        ["Commodity DeltaCharge High", "scalar"],
    ],
    groupby=["Group"],
    hide_zeros=True,
    calc_params=calc_params,
)

result1 = ds.compute(request1)

# print(result1) #<-- uncomment to see

request2 = dict(
    measures=[
        ["Commodity DeltaCharge Low", "scalar"],
        ["Commodity DeltaCharge Medium", "scalar"],
        ["Commodity DeltaCharge High", "scalar"],
    ],
    groupby=["Group"],
    hide_zeros=True,
)

result2 = ds.compute(request2)

# print(result2) #<-- uncomment to see
