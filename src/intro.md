# Introduction

**`ultibi`** is a free python library by **Ultima**.

This user guide's primary focus is a very specific case - **[Fundamental Review of the Trading Book's Standardised Approach](https://en.wikipedia.org/wiki/Fundamental_Review_of_the_Trading_Book)**. For a general usecase refer to the general user guide(TBA). Here we will focus on FRTB only. In general **`ultibi`** is a python interface of **Ultima**, a service which allows you to define, compute and breakdown the key metrics for your data.

# Why to use `ultibi`

- The calculation goes as per **[FRTB SA Paper](https://www.bis.org/bcbs/publ/d457.pdf)** (Note: `ultibi` is not (yet) certified by ISDA. Always check the output against your own interpretation of the regulation) and aims to be fully compliant(although not certified). **`ultibi`** supports **[CRR2](https://www.eba.europa.eu/regulation-and-policy/single-rulebook/interactive-single-rulebook/108255)** parameter set out of the box. Switch between the two is as easy as setting `jurisdiction` to `CRR2` or `BCBS`.

- You can breakdown and drillthrough your computation

- `ultibi` is very flexible and allows you to override any of the prescribed parameters (such as `girr_delta_rho_infl_base_low`) via `calc_params` argument. This essentually means that you can define your own parameter sets as per any regulatory requirements (eg non BCBS/CRR2). This also means that you can **stress test** against changes in the values of the prescribed (aka hard coded by ISDA) parameters.

- Everything you need for analysis: [Filtering](./filters.md), [Overriding](./override.md), [Adding Trades](./add_row.md) and so on.

- Blazingly [fast](./performace.md).

### Supported measures

CSR Sec CTP CVRdown

CSR Sec CTP CVRup

CSR Sec CTP Curvature Kb High

CSR Sec CTP Curvature Kb Low

CSR Sec CTP Curvature Kb Medium

CSR Sec CTP Curvature KbMinus High

CSR Sec CTP Curvature KbMinus Low

CSR Sec CTP Curvature KbMinus Medium

CSR Sec CTP Curvature KbPlus High

CSR Sec CTP Curvature KbPlus Low

CSR Sec CTP Curvature KbPlus Medium

CSR Sec CTP Curvature Sb High

CSR Sec CTP Curvature Sb Low

CSR Sec CTP Curvature Sb Medium

CSR Sec CTP CurvatureCharge High

CSR Sec CTP CurvatureCharge Low

CSR Sec CTP CurvatureCharge MAX

CSR Sec CTP CurvatureCharge Medium

CSR Sec CTP CurvatureDelta

CSR Sec CTP CurvatureDelta_Weighted

CSR Sec CTP DeltaCharge High

CSR Sec CTP DeltaCharge Low

CSR Sec CTP DeltaCharge MAX

CSR Sec CTP DeltaCharge Medium

CSR Sec CTP DeltaKb High

CSR Sec CTP DeltaKb Low

CSR Sec CTP DeltaKb Medium

CSR Sec CTP DeltaSb

CSR Sec CTP DeltaSens

CSR Sec CTP DeltaSens Weighted

CSR Sec CTP PnLdown

CSR Sec CTP PnLup

CSR Sec CTP VegaCharge High

CSR Sec CTP VegaCharge Low

CSR Sec CTP VegaCharge MAX

CSR Sec CTP VegaCharge Medium

CSR Sec CTP VegaKb High

CSR Sec CTP VegaKb Low

CSR Sec CTP VegaKb Medium

CSR Sec CTP VegaSb

CSR Sec CTP VegaSens

CSR Sec CTP VegaSens Weighted

CSR Sec nonCTP CVRdown

CSR Sec nonCTP CVRup

CSR Sec nonCTP Curvature Kb High

CSR Sec nonCTP Curvature Kb Low

CSR Sec nonCTP Curvature Kb Medium

CSR Sec nonCTP Curvature KbMinus High

CSR Sec nonCTP Curvature KbMinus Low

CSR Sec nonCTP Curvature KbMinus Medium

CSR Sec nonCTP Curvature KbPlus High

CSR Sec nonCTP Curvature KbPlus Low

CSR Sec nonCTP Curvature KbPlus Medium

CSR Sec nonCTP Curvature Sb High

CSR Sec nonCTP Curvature Sb Low

CSR Sec nonCTP Curvature Sb Medium

CSR Sec nonCTP CurvatureCharge High

CSR Sec nonCTP CurvatureCharge Low

CSR Sec nonCTP CurvatureCharge MAX

CSR Sec nonCTP CurvatureCharge Medium

CSR Sec nonCTP CurvatureDelta

CSR Sec nonCTP CurvatureDelta Weighted

CSR Sec nonCTP DeltaCharge High

CSR Sec nonCTP DeltaCharge Low

CSR Sec nonCTP DeltaCharge MAX

CSR Sec nonCTP DeltaCharge Medium

CSR Sec nonCTP DeltaKb High

CSR Sec nonCTP DeltaKb Low

CSR Sec nonCTP DeltaKb Medium

CSR Sec nonCTP DeltaSb

CSR Sec nonCTP DeltaSens

CSR Sec nonCTP DeltaSens Weighted

CSR Sec nonCTP PnLdown

CSR Sec nonCTP PnLup

CSR Sec nonCTP TotalCharge High

CSR Sec nonCTP TotalCharge Low

CSR Sec nonCTP TotalCharge MAX

CSR Sec nonCTP TotalCharge Medium

CSR Sec nonCTP VegaCharge High

CSR Sec nonCTP VegaCharge Low

CSR Sec nonCTP VegaCharge MAX

CSR Sec nonCTP VegaCharge Medium

CSR Sec nonCTP VegaKb High

CSR Sec nonCTP VegaKb Low

CSR Sec nonCTP VegaKb Medium

CSR Sec nonCTP VegaSb

CSR Sec nonCTP VegaSens

CSR Sec nonCTP VegaSens Weighted

CSR nonSec CVRdown

CSR nonSec CVRup

CSR nonSec Curvature Kb High

CSR nonSec Curvature Kb Low

CSR nonSec Curvature Kb Medium

CSR nonSec Curvature KbMinus High

CSR nonSec Curvature KbMinus Low

CSR nonSec Curvature KbMinus Medium

CSR nonSec Curvature KbPlus High

CSR nonSec Curvature KbPlus Low

CSR nonSec Curvature KbPlus Medium

CSR nonSec Curvature Sb High

CSR nonSec Curvature Sb Low

CSR nonSec Curvature Sb Medium

CSR nonSec CurvatureCharge High

CSR nonSec CurvatureCharge Low

CSR nonSec CurvatureCharge MAX

CSR nonSec CurvatureCharge Medium

CSR nonSec CurvatureDelta

CSR nonSec CurvatureDeltaWeighted

CSR nonSec DeltaCharge High

CSR nonSec DeltaCharge Low

CSR nonSec DeltaCharge MAX

CSR nonSec DeltaCharge Medium

CSR nonSec DeltaKb High

CSR nonSec DeltaKb Low

CSR nonSec DeltaKb Medium

CSR nonSec DeltaSb

CSR nonSec DeltaSens

CSR nonSec DeltaSens Weighted

CSR nonSec PnLdown

CSR nonSec PnLup

CSR nonSec TotalCharge High

CSR nonSec TotalCharge Low

CSR nonSec TotalCharge MAX

CSR nonSec TotalCharge Medium

CSR nonSec VegaCharge High

CSR nonSec VegaCharge Low

CSR nonSec VegaCharge MAX

CSR nonSec VegaCharge Medium

CSR nonSec VegaKb High

CSR nonSec VegaKb Low

CSR nonSec VegaKb Medium

CSR nonSec VegaSb

CSR nonSec VegaSens

CSR nonSec VegaSens Weighted

CSR_secCTP_TotalCharge_High

CSR_secCTP_TotalCharge_Low

CSR_secCTP_TotalCharge_Medium

Commodity CVRdown

Commodity CVRup

Commodity Curvature Kb High

Commodity Curvature Kb Low

Commodity Curvature Kb Medium

Commodity Curvature KbMinus High

Commodity Curvature KbMinus Low

Commodity Curvature KbMinus Medium

Commodity Curvature KbPlus High

Commodity Curvature KbPlus Low

Commodity Curvature KbPlus Medium

Commodity Curvature Sb High

Commodity Curvature Sb Low

Commodity Curvature Sb Medium

Commodity CurvatureCharge High

Commodity CurvatureCharge Low

Commodity CurvatureCharge MAX

Commodity CurvatureCharge Medium

Commodity CurvatureDelta

Commodity CurvatureDelta Weighted

Commodity DeltaCharge High

Commodity DeltaCharge Low

Commodity DeltaCharge MAX

Commodity DeltaCharge Medium

Commodity DeltaKb High

Commodity DeltaKb Low

Commodity DeltaKb Medium

Commodity DeltaSb

Commodity DeltaSens

Commodity DeltaSens Weighted

Commodity PnLdown

Commodity PnLup

Commodity TotalCharge High

Commodity TotalCharge Low

Commodity TotalCharge MAX

Commodity TotalCharge Medium

Commodity VegaCharge High

Commodity VegaCharge Low

Commodity VegaCharge MAX

Commodity VegaCharge Medium

Commodity VegaKb High

Commodity VegaKb Low

Commodity VegaKb Medium

Commodity VegaSb

Commodity VegaSens

Commodity VegaSens Weighted

DRC Charge

DRC Sec nonCTP CapitalCharge

DRC Sec nonCTP GrossJTD

DRC Sec nonCTP GrossJTD Scaled

DRC Sec nonCTP HBR

DRC Sec nonCTP NetLongJTD

DRC Sec nonCTP NetLongJTD Weighted

DRC Sec nonCTP NetShortJTD

DRC Sec nonCTP NetShortJTD Weighted

DRC nonSec CapitalCharge

DRC nonSec GrossJTD

DRC nonSec GrossJTD Scaled

DRC nonSec HBR

DRC nonSec NetAbsShortJTD Weighted

DRC nonSec NetLongJTD

DRC nonSec NetLongJTD Weighted

DRC nonSec NetShortJTD

EQ CVRdown

EQ CVRup

EQ Curvature Kb High

EQ Curvature Kb Low

EQ Curvature Kb Medium

EQ Curvature KbMinus High

EQ Curvature KbMinus Low

EQ Curvature KbMinus Medium

EQ Curvature KbPlus High

EQ Curvature KbPlus Low

EQ Curvature KbPlus Medium

EQ Curvature Sb High

EQ Curvature Sb Low

EQ Curvature Sb Medium

EQ CurvatureCharge High

EQ CurvatureCharge Low

EQ CurvatureCharge MAX

EQ CurvatureCharge Medium

EQ CurvatureDelta

EQ CurvatureDelta_Weighted

EQ DeltaCharge High

EQ DeltaCharge Low

EQ DeltaCharge MAX

EQ DeltaCharge Medium

EQ DeltaKb High

EQ DeltaKb Low

EQ DeltaKb Medium

EQ DeltaSb

EQ DeltaSens

EQ DeltaSens Weighted

EQ PnLdown

EQ PnLup

EQ TotalCharge High

EQ TotalCharge Low

EQ TotalCharge Medium

EQ VegaCharge High

EQ VegaCharge Low

EQ VegaCharge MAX

EQ VegaCharge Medium

EQ VegaKb High

EQ VegaKb Low

EQ VegaKb Medium

EQ VegaSb

EQ VegaSens

EQ VegaSens Weighted

Exotic RRAO Charge

Exotic RRAO Notional

FX CVRdown

FX CVRup

FX Curvature Kb

FX Curvature KbMinus

FX Curvature KbPlus

FX Curvature Sb

FX CurvatureCharge High

FX CurvatureCharge Low

FX CurvatureCharge MAX

FX CurvatureCharge Medium

FX CurvatureDelta

FX CurvatureDelta Weighted

FX DeltaCharge High

FX DeltaCharge Low

FX DeltaCharge MAX

FX DeltaCharge Medium

FX DeltaKb

FX DeltaSb

FX DeltaSens

FX DeltaSens Weighted

FX PnLdown

FX PnLup

FX TotalCharge High

FX TotalCharge Low

FX TotalCharge Medium

FX VegaCharge High

FX VegaCharge Low

FX VegaCharge MAX

FX VegaCharge Medium

FX VegaKb High

FX VegaKb Low

FX VegaKb Medium

FX VegaSb

FX VegaSens

FX VegaSens Weighted

GIRR CVRdown

GIRR CVRup

GIRR Curvature Kb

GIRR Curvature KbMinus

GIRR Curvature KbPlus

GIRR Curvature Sb

GIRR CurvatureCharge High

GIRR CurvatureCharge Low

GIRR CurvatureCharge MAX

GIRR CurvatureCharge Medium

GIRR CurvatureDelta

GIRR CurvatureDelta Weighted

GIRR DeltaCharge High

GIRR DeltaCharge Low

GIRR DeltaCharge MAX

GIRR DeltaCharge Medium

GIRR DeltaKb High

GIRR DeltaKb Low

GIRR DeltaKb Medium

GIRR DeltaSb

GIRR DeltaSens

GIRR DeltaSens Weighted

GIRR PnLdown

GIRR PnLup

GIRR TotalCharge High

GIRR TotalCharge Low

GIRR TotalCharge Medium

GIRR VegaCharge High

GIRR VegaCharge Low

GIRR VegaCharge MAX

GIRR VegaCharge Medium

GIRR VegaKb High

GIRR VegaKb Low

GIRR VegaKb Medium

GIRR VegaSb

GIRR VegaSens

GIRR VegaSens Weighted

GrossJTD

Notional

Other RRAO Charge

Other RRAO Notional

PnL_Down

PnL_Up

RRAO Charge

RiskWeights

SA Charge

SBM Charge

SBM Charge High

SBM Charge Low

SBM Charge Medium

SensitivitySpot

Sensitivity_025Y

Sensitivity_05Y

Sensitivity_10Y

Sensitivity_15Y

Sensitivity_1Y

Sensitivity_20Y

Sensitivity_2Y

Sensitivity_30Y

Sensitivity_3Y

Sensitivity_5Y
