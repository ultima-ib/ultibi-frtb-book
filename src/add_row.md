# Add Rows

`ultibi`'s request suppors adding rows(in our case Trades). This is a perfect functionality to have in your toolset, especially for a super quick What If analysis.

## Examples

An example of a request with `add_row` looks like this:

```python
{{#include ./examples/frtb_add_row.py}}
print(result1)
print(result2)
```

## Explanation

If you set `prepare` to true be prepared to provide all the required columns to assign weights.
