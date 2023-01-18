# Calc Params

ultibi allows you to override parameters of the regulation, which in turn allows you to define your own parameter sets. For example if a regulatory set is not yet supported - just override parameters which are different in `"calc_params"` part of your request.

## What you can override

Use `.calc_params` attribute to get the list of overridable parameters.

```python
for calc_param in dataset.calc_params:
    print(calc_param["name"], " - ", calc_param["hint"])
```

## Explanation

Most of these are self explanatory. However, one needs to understand what exactly some of those do:

1. Some calc_params **end** with **\_base** and some with **\_low/\_medium/\_high**. Those which end with **\_base** (eg. `com_delta_rho_diff_loc_base`) are *components of an actual rho*. For example `com_delta_rho_diff_loc_base` is (a float) and is part of three components which are multiplied to produce a commodity inner bucket rho as per `21.83.3`. This has one important implication. **Low/High function as per paragraph `21.6` in the [text](https://www.bis.org/bcbs/publ/d457.pdf) will be applied after this multiplication.** On the other hand, those calc_params which end with **\_low/\_medium/\_high** (eg `girr_delta_gamma_low`) will be used as they are.

1. Those calc_params (eg `com_delta_diff_cty_rho_per_bucket_base`) which are lists are usually per bucket, where index of the item indicates the number of the bucket.

1. `jurisdiction` - currently `BCBS` or `CRR2` - points to which parameter set (rhos, gammas etc) to be used by default. Also for **FX** if `reporting_ccy` is not provided

1. `reporting_ccy` - used for **FX**. Only those **FX** delta/curvature sensitivites where RiskFactor is XXXCCY (where CCY is the reporting_ccy) will be used for calculation. (eg if reporting_ccy is USD, GBPUSD will be used, but GBPEUR will not - this applies for Delta and Curvature calculations only).

1. You have to be very careful with the way to provide a `calc_param` in your request, especially for vectors and matrixes. use `json.dumps`. Follow examples below. 'v' is always 1.

## Examples

A request with `calc_params` looks like this. This is an arbitrary example just for illustrative purposes:

```python
{{#include ./examples/frtb_calc_params.py}}
print(result1)
print(result2)
```

## If a parameters could not get parsed

Currently, if your passed calc_param could not get parsed into a correct value (eg you provided float instead of a vector) - it will **silently** fall back to the defaulted value of the `jurisdiction`. **This will be changed in the next release to return an error to avoid ambiguity**.
