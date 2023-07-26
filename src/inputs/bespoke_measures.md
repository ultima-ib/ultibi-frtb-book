# Define your own Measures

One of the most powerful features of this Cube is the fact that you can define you own measures/calculations.

Please read the **[this article](https://medium.com/@anatoly.bugakov/ultibi-perform-custom-bespoke-dataframe-operation-through-a-ui-44eb10bbef2b)** for details.

 There are two kinds of **Calculators**:

1) *Standard Calculator* returns a polars expression. Use this when you can.

2) *Custom Calculator* returns a Polars Series. It's flexible but is slower due to the code executing in `Python` and therefore locking the GIL.

There are two kinds of **Measures**:

1) *BaseMeasure* executed within .filter().groupby().agg() context.
2) *DependantMeasure* executed within .with_columns() context, but after underlying BaseMeasures were executed (in their respective context).

## Example
**Note 1:** In this example the `kwargs` are `parameters` will be passed to your function through the [request](./calculation/calculate.md). See the chapter on [Calc Params](./calc_params.md) 

**Note 2:** make sure your function signatures are exactly as per the example
```python
{{#include ../examples/inputs/bespoke.py}}

ds.ui()
```
