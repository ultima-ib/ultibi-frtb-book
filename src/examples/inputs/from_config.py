import ultibi as ul

# You can set up a config and we will take care of
# castings, joins etc
ds = ul.FRTBDataSet.from_config_path("./data/frtb/datasource_config.toml")