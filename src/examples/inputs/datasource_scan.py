import polars as pl
import ultibi as ul

# Note that the LazyFrame query must start with scan_
# and must've NOT been collected
scan = pl.scan_csv("./data/frtb/Delta.csv", dtypes={"SensitivitySpot": pl.Float64})
dsource = ul.DataSource.scan(scan)
ds = ul.DataSet.from_source(dsource)
