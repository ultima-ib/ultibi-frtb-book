## Data Source Config

In principle, you are free to enrich this structure with as many columns as you want (for example Desk, Legal Entity etc). You can either do this manually or use `from_config`. Check out an example with explanations of each field: [datasource_config.toml](https://ultima-bi.s3.eu-west-2.amazonaws.com/frtb/datasource_config.toml).

```python
{{#include ../examples/inputs/from_config.py}}
print(ds.frame(None))
```

## Validate (work in progress)

If you are missing a required column you will get a runtime error during the execuiton of your request. Alternatively, call `.validate()`` on your dataset. It checks if every required column for every availiable calculation is present. Note: If you **can** guarantee your particular calculation would not require the missing columns you can proceed at your own risk!

```python
{{#include ../examples/frtb_validate.py}}
```
