# Calculation

## Before you run

Before you specify what you want to calculate **make sure the measure/risk metric you are interested in is present in the dataset**:

```python
print( {{#include ./examples/frtb_calculate.py:5:5}} )
```

What you get there is a `dict`. The **keys** are measures' name. For example `SensitivitySpot` or `FX DeltaCharge Low`. The **items** indicate if there is any *restriction on aggregation method*, where `scalar` is a special method explained below. If `None`, you are free to use any of the availiable:

```python
print( {{#include ./examples/frtb_calculate.py:6:6}} )
```

Note that any numeric column automatically considered a measure (eg `SensitivitySpot`). These measures can be aggregated any way you want for a given level, say Desk. In other words, for a given Desk you can find the mean, max, min or sum (etc etc) of `SensitivitySpot`. On the other hand, you can **not** find mean, max, min (etc etc) of `FX DeltaCharge Low`. This wouldn't make sence since `FX DeltaCharge Low` is simply a single number defined by the regulation. Hence we call such aggregation method **`scalar`** and we **restrict** you to use only this method.

Also, make sure that columns which appear in measures, grouby and filters are present as well.

## Run

Now we are good to form the request which we need. Say, we want to understand the `DRC` capital charge and all intermediate results, for every combination of `Desk` - `BucketBCBS`.

```python
{{#include ./examples/frtb_calculate.py:8:27}}
```

Note: if you don't care about level of aggregation and just want a total say DRC Capital Charge for your portfolio, just provide an extra column to your portfolio, name it `"Total"`(for exmaple) and set all values in the columns as `"Total"`. Then do `groupby=["Total"]`. Above request has two **optional** parameters which we haven't talked about yet: `hide_zeros` and `calc_params`. `hide_zeros` simply removes rows **from the result** where each measure is 0, and `calc_params` allows you to override default parameters such as `jurisdiction`, `reporting_ccy`, `girr_delta_rho_diff_curve_base` (and many many others. We will talk about in [analysis](./whatif.md) chapter) etc.

Valide that you've formed a legitimate request (ie no compulsory field is missing, datatypes are correct etc):

```python
{{#include ./examples/frtb_calculate.py:29:29}}
print(request)
```

Finally, to execute(depreciated, do not use):

```python
{{#include ./examples/frtb_calculate.py:32:32}}
print(result)
```

Or, preferred way:

```python
{{#include ./examples/frtb_calculate.py:36:36}}
print(result)
print("Type: ", type(result))
```

Notice the returned object is a polars DataFrame. You can then do whatever you want with it. Print (to set how many columns you want to print make sure to use polars [config](https://pola-rs.github.io/polars/py-polars/html/reference/config.html)), or any on the [I/O](https://pola-rs.github.io/polars/py-polars/html/reference/io.html): save to csv, parquet, database etc.
