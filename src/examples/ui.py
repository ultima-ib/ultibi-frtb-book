import ultibi as ul
import time
import os

os.environ["RUST_LOG"] = "info"
os.environ["ADDRESS"] = "0.0.0.0:8000"

start_time = time.time()
ds = ul.FRTBDataSet.from_config_path(
    "datasource_config.toml", collect=True, prepare=True
)
print("--- Read DF time: %s seconds ---" % (time.time() - start_time))
