import polars as pl
import ultibi as ul

pl.Config.set_tbl_rows(100)
pl.Config.set_tbl_cols(14)

# First, let's mock up a portfolio of 15 trades
# Note: we will ask ultibi to assign risk weight for us as per the regulation
# As such, we need to provide all the columns required for weights assignments,
# even if they are not used.
# fmt: off
data = {
# Optional but useful column. We will aggregate at the level of "Group"
"Group": ["Ultima"]*15,
# Delta represents both Delta and Curvature risk. Vega is for Vega only
"RiskCategory":	["Delta","Delta","Delta","Delta","Vega","Vega","Vega","Vega",
                 "Delta","Delta","Delta","Delta","Delta","Delta","Delta"],
"RiskClass": ["FX",	"FX", "FX",	"FX","FX","FX","FX","FX","FX","FX","FX","FX","FX",
              "FX","FX"],
# FX Risk Factor must be of CCY1/CCY2 format
"RiskFactor":["GBPUSD","BRLUSD","BRLUSD","JPYEUR","GBPUSD","GBPUSD","THOUSD","JPYEUR","EUREUR","EURUSD","GBPEUR","GBPUSD","EURUSD","AZNUSD","EURUSD"],
# We leave it as none because ultibi fills nans on this column with RiskFactor for FX
"BucketBCBS": [None]*15,															
"BucketCRR2": [None]*15,
# RiskFactorType is not relevant to FX, but we still need to provide it 
"RiskFactorType": [""]*15,
"CreditQuality": [""]*15,	
# Cob and MaturityDate is not relevant to FX, but we still need to provide it 
"COB": ["2023-01-30"]*15,
"MaturityDate": ["2023-01-30"]*15,	
# These are our sensitivities
"PnL_Up":[1000.0,1000,1000,1000,None,None,None,None,None,None,None,None,None,None,None],										
"PnL_Down":[-1000.0,-1000,-1000,-1000,None,None,None,None,None,None,None,None,None,None,None],										
"SensitivitySpot":[123000,	123000,	123000,	123000, None,None,None,None,100,5,15,10,5,
                    -13.5,100],
"Sensitivity_05Y":[None,None,None,None,5000,5000,1000,None,None,None,None,None,None,None,None],							
"Sensitivity_1Y":[None,None,None,None,5000,5000,None,1000,None,None,None,None,None,None,None],								
"Sensitivity_3Y": [None,None,None,None,5000,5000,None,1000,None,None,None,None,None,
                    None,None],
"Sensitivity_5Y": [None,None,None,None,5000,5000,None,1000,None,None,None,None,None,
                    None,None],
"Sensitivity_10Y": [None,None,None,None,5000,5000,None,1000,None,None,None,None,None,
                    None,None],
# 21.98
"FxCurvDivEligibility":[True,True,None,None,None,None,None,None,None,None,None,None,None,None,None],
}	
# fmt: on
df = pl.DataFrame(data)

# Conver our frame into FRTB dataset, opting into sqrt 2 division as per 21.88
ds = ul.FRTBDataSet.from_frame(df, build_params={"fx_sqrt2_div": "true"})
# This will add SensWeights and CurvatureWeight columns to our dataset
ds.prepare()

request = dict(
    measures=[
        ["FX DeltaCharge Low", "scalar"],
        ["FX DeltaCharge Medium", "scalar"],
        ["FX DeltaCharge High", "scalar"],
        ["FX VegaCharge Low", "scalar"],
        ["FX VegaCharge Medium", "scalar"],
        ["FX VegaCharge High", "scalar"],
        ["FX CurvatureCharge Low", "scalar"],
        ["FX CurvatureCharge Medium", "scalar"],
        ["FX CurvatureCharge High", "scalar"],
    ],
    # Break down results by Group and BucketBCBS
    groupby=["Group", "BucketBCBS"],
    # Show totals for each Group (note in this example only 1)
    totals=True,
    # Hide rows where each result is 0
    hide_zeros=True,
    calc_params={
        "jurisdiction": "BCBS",
        # Apply 21.98
        "apply_fx_curv_div": "true",
    },
)

# Execute
result = ds.compute(request)
