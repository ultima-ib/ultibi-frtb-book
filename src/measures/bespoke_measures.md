# Define your own Measures

One of the most powerful features of this Cube is the fact that you can define you own measures/calculations. If you work in pure `Rust`, you don't need to worry about how you create bespoke measures, since you are not bounded by GIL(see `frtb_engine` for examples).

In python, however, we need to consider certain limitations of the GIL. Please read the **[this article](https://medium.com/@anatoly.bugakov/ultibi-perform-custom-bespoke-dataframe-operation-through-a-ui-44eb10bbef2b)** for details.

First, we need to understand distinction between a **Measure** and **Calculator**. **Measure** is simply a wrapper around a **Calculator** (so that each measure owns one calculator), with some additional attributes (such as *name*).

There are two kinds of **Calculators**:

1. *Standard Calculator* returns a polars expression. Use this when you can.

1. *Custom Calculator* returns a Polars Series. It's flexible but is slower due to the code executing in `Python` and therefore locking the GIL.

There are two kinds of **Measures**:

1. *BaseMeasure* executed within .filter().groupby().agg() context.

1. *DependantMeasure* executed within .with_columns() context, but after underlying BaseMeasures were executed (in their respective context).

## Example

**Note 1:** In this example the `kwargs` are `parameters` will be passed to your function through the [request](../calculation/calculate.md). See the chapter on [Calc Params](../calculation/whatif/calc_params.md)

**Note 2:** make sure your function signatures are exactly as per the example

```python
{{#include ../examples/inputs/bespoke.py}}

ds.ui()
```
