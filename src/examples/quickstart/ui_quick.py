import ultibi as ul
import polars as pl
import os

os.environ["RUST_LOG"] = "info"  # enable logs
os.environ["ADDRESS"] = "0.0.0.0:8000"  # host on this address

# Read Data
# for more details: https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.read_csv.html
df = pl.read_csv("data/titanic.csv")

# Convert it into an Ultibi DataSet
ds = ul.DataSet.from_frame(df)
