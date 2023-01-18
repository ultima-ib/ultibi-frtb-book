import ultibi as ul

ds = ul.FRTBDataSet.from_config_path("./data/frtb/datasource_config.toml")
try:
    ds.validate()
except ul.NoDataError as e:
    print(
        "One of key columns is missing. Be carefull if you wish to proceed "
        "without it. Error: ",
        e,
    )
print("Complete")
