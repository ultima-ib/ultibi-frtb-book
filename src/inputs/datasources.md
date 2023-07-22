# Input and Data Sources

## In Memory
If your data fits into process memory - use that. It's fast. 
```python
{{#include ../examples/inputs/datasource_inmemory.py}}

ds.ui()
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