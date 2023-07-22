## Ultima DataSet

First step is to create a DataSet from your portfolio data. Think of a DataSet as a DataFrame with some special pre defined functions (eg "FX Delta Capital Charge").

## From Frame

In order to use our library you need to convert your portfolio into [polars](https://pola-rs.github.io/polars-book/user-guide/) [Dataframe](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/index.html). You can either do this yourself(using any of the countless [IO](https://pola-rs.github.io/polars-book/user-guide/howcani/io/csv.html) operations supported. Note polars also supports [from_pandas](https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.from_pandas.html) and [from_arrow](https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.from_arrow.html)) or use a [config](#data-source-config).

```python
{{#include ../examples/frtb_input.py:0:8}}
print(ds.frame(None))
```

## Data Source Config

In principle, you are free to enrich this structure with as many columns as you want (for example Desk, Legal Entity etc). You can either do this manually or use `from_config`. Check out an example with explanations of each field: [datasource_config.toml](https://ultima-bi.s3.eu-west-2.amazonaws.com/frtb/datasource_config.toml).

```python
{{#include ../examples/frtb_input.py:11:14}}
print(ds.frame(None))
```

## Validate

If you are missing a required column you will get a runtime error during the execuiton of your request. Alternatively, call .validate() on your dataset. It checks if every required column for every availiable calculation is present. Note: If you **can** guarantee your particular calculation would not require the missing columns you can proceed at your own risk!

```python
{{#include ./examples/frtb_validate.py}}
```
