# with UI

To spin up the Cube/Pivot UI

```python
{{#include ../examples/quickstart/ui_quick.py}}

# By default (might change in the future)
# Fields are Utf8 (non numerics) and integers, but you can configure it
# through the config. See `Input and Data Sources` section.
# Measures are numeric columns.
ds.ui()
```
