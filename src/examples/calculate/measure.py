import ultibi as ul
import polars as pl

df = pl.DataFrame(
            {
                "a": [1, 2, -3],
                "b": [4, 5, 6],
                "c": ["z", "z", "w"],
                "d": ["k", "y", "s"],
            }
        )

ds = ul.DataSet.from_frame(df, measures=["a"])

assert ds.measures == dict(a=None)