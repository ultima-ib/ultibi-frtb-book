import ultibi as ul
import polars as pl

scan = pl.read_csv("../frtb_engine/data/frtb/Delta.csv", 
                           dtypes={"SensitivitySpot": pl.Float64})
dsource = ul.DataSource.inmemory(scan)
ds = ul.DataSet.from_source(dsource)
ds.prepare() # .prepare() is only relevant to FRTB dataset currently