# Define your own Measures in Rust and expose to Python API

No GIL, meaning your measures will run in parallel.

Check out [this example](https://github.com/ultima-ib/ultima/tree/master/templates/rust_py_measure)

Leveraging on [pyo3-polars](https://github.com/pola-rs/pyo3-polars) you can define your own function, in `Rust`, and expose it to Python. 

# Why? 
When you want to create an **extension** for `ultibi` cubes, and want your users to use it in *pure python*.

Note **my_rusty_measures** below:

```python
import ultibi as ul
import polars as pl
from rust_py_measure import my_rusty_measures

df = pl.DataFrame(
            {
                "a": [1, 2, -3],
                "b": [4, 5, 6],
                "c": ["z", "z", "w"],
                "d": ["k", "y", "s"],
            }
        )

ds = ul.DataSet.from_frame(df, bespoke_measures=my_rusty_measures)

print(ds.measures)
request = dict(measures=[["MyRustyMeasure", "scalar"]], groupby=["c"])
result = ds.compute(request)
ds.ui()
```