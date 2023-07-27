# Assign Weights/Prepare

**Currently this section only applies to FRTBDataSet**. In the future `python` users will be able to define their own, custom `prepare` functions too.

Prepare is a **fixed** calculation which happens with every request for scans/db DataSources. For InMemory it happens only when you call `.prepare()`.

`from_config()` call `.prepare()` depending on `source_type`.

A good usecase for that is to assign weights column to your data, as per FRTB regulation for example. **Make sure you assign weights before doing any computations**:

```python
{{#include ../examples/calculate/prepare.py}}
print(diff_frame.columns)
```

You will get an error if you try to assign twice. Now, let's see what happened. We will need a little helper function:

At the time of writing this returns 6 new columns(names of the columns might change slightly but the meaning will always be the same):

| Column Name               | Explanation                                                                                                                  |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------|
| SensWeights               | List of weights, one for each tenor. Eg \[1,1,1,1,1\] for any Vega risk.                                                       |
|  CurvatureRiskWeight      | Simply max of SensWeights if PnL Up or Down was provided, otherwise NULL. This is how we identify Curvature eligible trades. |
|  SensWeightsCRR2          | Same as SensWeights but under CRR2 rules.                                                                                    |
|  CurvatureRiskWeightCRR2  | Same logic as BCBS                                                                                                           |
|  ScaleFactor              | DRC scailing: yearfrac between COB and MaturityDate                                                                          |
|  SeniorityRank            | Mapping used internaly for DRC offsetting                                                                                    |
