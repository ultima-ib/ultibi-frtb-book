# FRTB SA - Input format

Any calculation/function needs inputs. In case of FRTB SA the **input is your portfolio sensitivities at trade level**. Currently expected format for the sensitivities is like this: [Delta.csv](https://ultima-bi.s3.eu-west-2.amazonaws.com/frtb/Delta.csv). This format is very similar to the industry standard [CRIF](https://www.isda.org/a/aBzTE/The-Future-of-Risk-Capital-and-Margin.pdf). Coming soon full CRIF support. As you can see, this file is your Sensitivities at Trade-RiskFactor-Tenor level.

In our examples we will also be using an optional `hierarchies` file [hms.csv](https://ultima-bi.s3.eu-west-2.amazonaws.com/frtb/hms.csv). Hierarchies simply define which `Book` belongs to where in terms of Business and/or Legal structure (eg which Desk or Legal Entity).

Finally, we need [TradeAttributes.csv](https://ultima-bi.s3.eu-west-2.amazonaws.com/frtb/TradeAttributes.csv). It is similar to our Delta Sensis but the data here is at Trade level only. Ie Notional, Product/Derivative Type, RRAO Flags etc etc.

# Defenitions

Note that the **[FRTB SA Paper](https://www.bis.org/bcbs/publ/d457.pdf)** actually well defines what a "RiskFactor" is and the formulas for "Sensitivities". See paragraphs `21.8-21.19` and `21.19-21.26` respectively.

### Expected Columns Explanation - Risk

Table below will outline which columns are expected, the useage and meaning behind them. This table might get outdated. Always check `Delta.csv`.

| ColumnName                 | Expected for Weights Assignments | Expected for Calculation (past weights/scailing assignments) | Restrictions on values                                                                   | Where used                                           | Explanation                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------|----------------------------------|--------------------------------------------------------------|------------------------------------------------------------------------------------------|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| COB                        | Y                                | N                                                            | N                                                                                        | Used with MaturityDate to assign DRC Scailing Factor |                                                                                                                                                                                                                                                                                                                                                                                               |
| TradeId                    | N                                | Y                                                            | N                                                                                        | RRAO                                                 |                                                                                                                                                                                                                                                                                                                                                                                               |
| RiskCategory               | Y                                | Y                                                            | Delta or Vega                                                                            | All Risk Calculations                                | Note: Curvature goes under Delta                                                                                                                                                                                                                                                                                                                                                              |
| RiskClass                  | Y                                | Y                                                            | DRC_Sec_nonCTP/DRC_nonSec/CSR_Sec_nonCTP/Commodity/CSR_Sec_CTP/CSR_nonSec/Equity/FX/GIRR | All Risk Calculations(except RRAO)                   |                                                                                                                                                                                                                                                                                                                                                                                               |
| RiskFactor                 | Y                                | Y                                                            |                                                                                          | All Risk Calculations(except RRAO)                   | Different meaning depending on RiskClass. See Delta.csv for correct value for your particular RiskClass. Note: for FX convention used XXXCCY where CCY is your reporting currency. Parameter reporting_ccy will filter out all lines where CCY doesn't match it's value. For jurisdiction BCBS XXXUSD only will be used (unless overriden with reporting_ccy), and similarly XXXEUR for CRR2. |
| RiskFactorType             | Y                                | Y                                                            | See Delta.csv                                                                            | All Risk Calculations(except RRAO)                   | Note: Different meaning depending on RiskClass. See Delta.csv for correct value for your particular RiskClass.                                                                                                                                                                                                                                                                                |
| CreditQuality              |                                  | N                                                            |                                                                                          | DRC nonSec and DRC Sec nonCTP                        | For DRC Sec nonCTP Joined with RiskFactorType with _ and then assigned via the table below. For DRC nonSec see respective table                                                                                                                                                                                                                                                               |
| MaturityDate               | Y                                | N                                                            |                                                                                          | Used with COB to assign DRC Scailing Factor          |                                                                                                                                                                                                                                                                                                                                                                                               |
| Tranche                    |                                  | Y                                                            |                                                                                          | DRC_Sec_nonCTP                                       |                                                                                                                                                                                                                                                                                                                                                                                               |
| CommodityLocation          |                                  | Y                                                            |                                                                                          | Commodity Delta                                      |                                                                                                                                                                                                                                                                                                                                                                                               |
| GirrVegaUnderlyingMaturity |                                  | Y                                                            |                                                                                          | GIRR Vega                                            |                                                                                                                                                                                                                                                                                                                                                                                               |
| BucketBCBS                 |                                  | Y                                                            | See Delta.csv                                                                            | All Risk Calculations(except RRAO)                   | Be careful, refer to Delta.csv Note: For FX if not provided will be derived using RiskFactor                                                                                                                                                                                                                                                                                                  |
| BucketCRR2                 |                                  | Y(if opt in CRR2)                                            | See Delta.csv                                                                            |                                                      | Note: Present because some CSR buckets are different between BCBS and CRR2                                                                                                                                                                                                                                                                                                                    |
| GrossJTD                   |                                  | Y                                                            |                                                                                          |                                                      |                                                                                                                                                                                                                                                                                                                                                                                               |
| PnL_Up                     |                                  | Y                                                            |                                                                                          |                                                      |                                                                                                                                                                                                                                                                                                                                                                                               |
| PnL_Down                   |                                  | Y                                                            |                                                                                          |                                                      |                                                                                                                                                                                                                                                                                                                                                                                               |
| SensitivitySpot            |                                  | Y                                                            |                                                                                          |                                                      |                                                                                                                                                                                                                                                                                                                                                                                               |
| Sensitivity_025Y           |                                  | Y                                                            |                                                                                          |                                                      |                                                                                                                                                                                                                                                                                                                                                                                               |
| Sensitivity_05Y            |                                  | Y                                                            |                                                                                          |                                                      | For Vega used as Option Maturity Tenor. For Delta as Risk Factor Tenor                                                                                                                                                                                                                                                                                                                        |
| Sensitivity_1Y             |                                  | Y                                                            |                                                                                          |                                                      | For Vega used as Option Maturity Tenor. For Delta as Risk Factor Tenor                                                                                                                                                                                                                                                                                                                        |
| Sensitivity_2Y             |                                  | Y                                                            |                                                                                          |                                                      |                                                                                                                                                                                                                                                                                                                                                                                               |
| Sensitivity_3Y             |                                  | Y                                                            |                                                                                          |                                                      | For Vega used as Option Maturity Tenor. For Delta as Risk Factor Tenor                                                                                                                                                                                                                                                                                                                        |
| Sensitivity_5Y             |                                  | Y                                                            |                                                                                          |                                                      | For Vega used as Option Maturity Tenor. For Delta as Risk Factor Tenor                                                                                                                                                                                                                                                                                                                        |
| Sensitivity_10Y            |                                  | Y                                                            |                                                                                          |                                                      | For Vega used as Option Maturity Tenor. For Delta as Risk Factor Tenor                                                                                                                                                                                                                                                                                                                        |
| Sensitivity_15Y            |                                  | Y                                                            |                                                                                          |                                                      |                                                                                                                                                                                                                                                                                                                                                                                               |
| Sensitivity_20Y            |                                  | Y                                                            |                                                                                          |                                                      |                                                                                                                                                                                                                                                                                                                                                                                               |
| Sensitivity_30Y            |                                  | Y                                                            |                                                                                          |                                                      |                                                                                                                                                                                                                                                                                                                                                                                               |
| CoveredBondReducedWeight   | Y(if you opted in via config)    | N                                                            |                                                                                          | Y or N                                               |                                                                                                                                                                                                                                                                                                                                                                                               |
| FxCurvDivEligibility       |                                  | Y                                                            |                                                                                          | Y or N                                               |


### Expected Columns Explanation - Trade attributes

| ColumnName  | Expected for Weights Assignments | Expected for Calculation (past weights/scailing assignments) | Restrictions on values | Where used | Explanation                             |
|-------------|----------------------------------|--------------------------------------------------------------|------------------------|------------|-----------------------------------------|
| TradeId     | N                                | Y                                                            | N                      | RRAO       |                                         |
| BookId      | N                                | N                                                            |                        |            | Not required. We use it to join hms.csv |
| EXOTIC_RRAO | N                                | Y                                                            |                        | RRAO       |                                         |
| OTHER_RRAO  | N                                | Y                                                            |                        | RRAO       |                                         |
| Notional    | N                                | Y                                                            |                        | RRAO       |

### DRC Sec nonCTP - CreditQiality+_+RiskFactorType Weights

| CreditQuality+_+RiskFactorType | DRC Sec  nonCTP Weight |
|--------------------------------|------------------------|
| AAA_SENIOR                     | 1.2                    |
| AA+_SENIOR                     | 1.2                    |
| AA_SENIOR                      | 2                      |
| AA-_SENIOR                     | 2.4                    |
| A+_SENIOR                      | 3.2                    |
| A_SENIOR                       | 4                      |
| A-_SENIOR                      | 4.8                    |
| BBB+_SENIOR                    | 6                      |
| BBB_SENIOR                     | 7.2                    |
| BBB-_SENIOR                    | 9.6                    |
| BB+_SENIOR                     | 11.2                   |
| BB_SENIOR                      | 12.8                   |
| BB-_SENIOR                     | 16                     |
| B+_SENIOR                      | 20                     |
| B_SENIOR                       | 24.8                   |
| B-_SENIOR                      | 30.4                   |
| CCC+_SENIOR                    | 36.8                   |
| CCC_SENIOR                     | 36.8                   |
| CCC-_SENIOR                    | 36.8                   |
| D_SENIOR                       | 100                    |
| UNDERATD_SENIOR                | 100                    |
| OTHER_SENIOR                   | 100                    |
| AAA_JUNIOR                     | 1.2                    |
| AA+_JUNIOR                     | 1.2                    |
| AA_JUNIOR                      | 2.4                    |
| AA-_JUNIOR                     | 3.2                    |
| A+_JUNIOR                      | 4.8                    |
| A_JUNIOR                       | 6.4                    |
| A-_JUNIOR                      | 9.6                    |
| BBB+_JUNIOR                    | 13.6                   |
| BBB_JUNIOR                     | 17.6                   |
| BBB-_JUNIOR                    | 26.4                   |
| BB+_JUNIOR                     | 37.6                   |
| BB_JUNIOR                      | 49.6                   |
| BB-_JUNIOR                     | 60                     |
| B+_JUNIOR                      | 72                     |
| B_JUNIOR                       | 84                     |
| B-_JUNIOR                      | 90.4                   |
| CCC+_JUNIOR                    | 100                    |
| CCC_JUNIOR                     | 100                    |
| CCC-_JUNIOR                    | 100                    |
| D_JUNIOR                       | 100                    |
| UNDERATD_JUNIOR                | 100                    |
| OTHER_JUNIOR                   | 100                    |
| A-1_JUNIOR                     | 1.2                    |
| A-1_SENIOR                     | 1.2                    |
| P-1_JUNIOR                     | 1.2                    |
| P-1_SENIOR                     | 1.2                    |
| A-2_JUNIOR                     | 4                      |
| A-2_SENIOR                     | 4                      |
| P-2_JUNIOR                     | 4                      |
| P-2_SENIOR                     | 4                      |
| A-3_JUNIOR                     | 8                      |
| A-3_SENIOR                     | 8                      |
| P-3_JUNIOR                     | 8                      |
| P-3_SENIOR                     | 8                      |
| UNDERATD_JUNIOR                | 100                    |
| UNDERATD_SENIOR                | 100                    |
| AAA_NONSENIOR                  | 1.2                    |
| AA+_NONSENIOR                  | 1.2                    |
| AA_NONSENIOR                   | 2.4                    |
| AA-_NONSENIOR                  | 3.2                    |
| A+_NONSENIOR                   | 4.8                    |
| A_NONSENIOR                    | 6.4                    |
| A-_NONSENIOR                   | 9.6                    |
| BBB+_NONSENIOR                 | 13.6                   |
| BBB_NONSENIOR                  | 17.6                   |
| BBB-_NONSENIOR                 | 26.4                   |
| BB+_NONSENIOR                  | 37.6                   |
| BB_NONSENIOR                   | 49.6                   |
| BB-_NONSENIOR                  | 60                     |
| B+_NONSENIOR                   | 72                     |
| B_NONSENIOR                    | 84                     |
| B-_NONSENIOR                   | 90.4                   |
| CCC+_NONSENIOR                 | 100                    |
| CCC_NONSENIOR                  | 100                    |
| CCC-_NONSENIOR                 | 100                    |
| D_NONSENIOR                    | 100                    |
| UNDERATD_NONSENIOR             | 100                    |
| OTHER_NONSENIOR                | 100                    |
| A-1_NONSENIOR                  | 1.2                    |
| P-1_NONSENIOR                  | 1.2                    |
| A-2_NONSENIOR                  | 4                      |
| P-2_NONSENIOR                  | 4                      |
| A-3_NONSENIOR                  | 8                      |
| P-3_NONSENIOR                  | 8                      |
| UNDERATD_NONSENIOR             | 100                    |
| D_NONSENIOR                    | 100                    |
| AAA_SUBORDINATE                | 1.2                    |
| AA+_SUBORDINATE                | 1.2                    |
| AA_SUBORDINATE                 | 2.4                    |
| AA-_SUBORDINATE                | 3.2                    |
| A+_SUBORDINATE                 | 4.8                    |
| A_SUBORDINATE                  | 6.4                    |
| A-_SUBORDINATE                 | 9.6                    |
| BBB+_SUBORDINATE               | 13.6                   |
| BBB_SUBORDINATE                | 17.6                   |
| BBB-_SUBORDINATE               | 26.4                   |
| BB+_SUBORDINATE                | 37.6                   |
| BB_SUBORDINATE                 | 49.6                   |
| BB-_SUBORDINATE                | 60                     |
| B+_SUBORDINATE                 | 72                     |
| B_SUBORDINATE                  | 84                     |
| B-_SUBORDINATE                 | 90.4                   |
| CC+_SUBORDINATE                | 100                    |
| CC_SUBORDINATE                 | 100                    |
| CC-_SUBORDINATE                | 100                    |
| D_SUBORDINATE                  | 100                    |
| UNDERATD_SUBORDINATE           | 100                    |
| OTHER_SUBORDINATE              | 100                    |
| A-1_SUBORDINATE                | 1.2                    |
| P-1_SUBORDINATE                | 1.2                    |
| A-2_SUBORDINATE                | 4                      |
| P-2_SUBORDINATE                | 4                      |
| A-3_SUBORDINATE                | 8                      |
| P-3_SUBORDINATE                | 8                      |
| UNDERATD_SUBORDINATE           | 100                    |
| D_SUBORDINATE                  | 100                    |


### DRC nonSec - BCBS CreditQiality Weights

|               |            |
|---------------|------------|
| CreditQuality | WeightBCBS |
| AAA           | 0.005      |
| AA            | 0.02       |
| A             | 0.03       |
| BBB           | 0.06       |
| BAA           | 0.06       |
| BB            | 0.15       |
| BA            | 0.15       |
| B             | 0.3        |
| CCC           | 0.5        |
| CAA           | 0.5        |
| CA            | 0.5        |
| UNRATED       | 0.15       |
| NORATING      | 0.15       |
| DEFAULTED     | 1          |
|               |            |
| CreditQuality | WeightCRR2 |
| AAA           | 0.005      |
| AA            | 0.005      |
| A             | 0.03       |
| BBB           | 0.06       |
| BAA           | 0.06       |
| BB            | 0.15       |
| BA            | 0.15       |
| B             | 0.3        |
| CCC           | 0.5        |
| CAA           | 0.5        |
| CA            | 0.5        |
| UNRATED       | 0.15       |
| NORATING      | 0.15       |
| DEFAULTED     | 1          |


