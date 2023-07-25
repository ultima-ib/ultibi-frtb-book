# Input and Data Sources

## In Memory
If your data fits into process memory - use that. It's fast. 
```python
{{#include ../examples/inputs/datasource_inmemory.py}}

ds.ui()
```

Same would be achieved with a `.from_frame()` shortcut.

Your data must be a [polars](https://pola-rs.github.io/polars-book/user-guide/) [Dataframe](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/index.html). You can either do this yourself(using any of the countless [IO](https://pola-rs.github.io/polars-book/user-guide/howcani/io/csv.html) operations supported, or using a [config](./input.md). Note polars also supports [from_pandas](https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.from_pandas.html) and [from_arrow](https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.from_arrow.html)) or use a [config](#data-source-config).

```python
{{#include ../examples/frtb_input.py:0:8}}
print(ds.frame(None))
```
## Scan 
If you can't hold all your data in the process memory, you can sacrifise performance for a Scan. 
```python
{{#include ../examples/inputs/datasource_scan.py}}

ds.ui()
```
Note:
- Naturally this option will be slower, because prior to computing your measures we will need to read the relevant bits of the data into the process memory, and if relevant, call .prepare().
- Scanning involves serialisation of the Lazy Frame, and hence the python version of your `polars` lib must be aligned to what we expect. At the time of writing it has to be `>=0.18.7`.

## DataBase - Work in Progress