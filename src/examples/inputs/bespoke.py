import ultibi as ul
import polars as pl
import os

os.environ["RUST_LOG"] = "info"  # enable logs
os.environ["ADDRESS"] = "0.0.0.0:8000"  # host on this address

# Read Data
# for more details: https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.read_csv.html
df = pl.read_csv("./data/titanic.csv")

# Let's add some Custom/Bespoke Calculations to our UI


# Standard Calculator
def survival_mean_age(kwargs: dict[str, str]) -> pl.Expr:
    """Mean Age of Survivals
    pl.col("survived") is 0 or 1
    pl.col("age") * pl.col("survived") - age of survived person, otherwise 0
    pl.col("survived").sum() - number of survived
    """
    return pl.col("age") * pl.col("survived") / pl.col("survived").sum()


# Also a Standard Calculator
def example_dep_calc(kwargs: dict[str, str]) -> pl.Expr:
    return pl.col("SurvivalMeanAge_sum") + pl.col("SouthamptonFareDivAge_sum")


# When we need more involved calculations we go for a Custom Calculator
def custom_calculator(srs: list[pl.Series], kwargs: dict[str, str]) -> pl.Series:
    """
    Southampton Fare/Age*multiplier
    """
    df = pl.DataFrame({"age": srs[0], "fare": srs[1], "e": srs[2]})
    # Add Indicator Column for Southampton
    df = df.with_columns(pl.when(pl.col("e") == "S").then(1).otherwise(0).alias("S"))
    multiplier = float(kwargs.get("multiplier", 1))
    res = df["S"] * df["fare"] / df["age"] * multiplier
    return res


# inputs for the custom_calculator srs param
inputs = ["age", "fare", "embarked"]
# We return Floats
res_type = pl.Float64
# We return a Series, not a scalar (which otherwise would be auto exploded)
returns_scalar = False

measures = [
    ul.BaseMeasure(
        "SouthamptonFareDivAge",
        ul.CustomCalculator(custom_calculator, res_type, inputs, returns_scalar),
        # (Optional) - we are only interested in Southampton, so
        # unless other measures requested we might as well filter
        # for Southampton only
        # However, if if multiple measures requested, their
        # precompute_filters will be joined as OR.
        [[ul.EqFilter("embarked", "S")]],
        # PARAMS tab of the UI
        calc_params=[ul.CalcParam("mltplr", "1", "float")],
    ),
    ul.BaseMeasure(
        "SurvivalMeanAge",
        ul.StandardCalculator(survival_mean_age),
        aggregation_restriction="sum",
    ),
    ul.DependantMeasure(
        "A_Dependant_Measure",
        ul.StandardCalculator(example_dep_calc),
        [("SurvivalMeanAge", "sum"), ("SouthamptonFareDivAge", "sum")],
    ),
]

# Convert it into an Ultibi DataSet
ds = ul.DataSet.from_frame(df, bespoke_measures=measures)
