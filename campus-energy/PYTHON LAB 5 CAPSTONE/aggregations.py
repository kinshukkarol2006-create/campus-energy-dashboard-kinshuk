import pandas as pd

# ------------------------------------------------
# DAILY TOTALS
# ------------------------------------------------
def calculate_daily_totals(df):
    # Ensure timestamp is datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Drop rows with bad timestamps
    df = df.dropna(subset=["timestamp"])

    # Set datetime index
    df = df.set_index("timestamp")

    # Daily total per building
    daily = df.groupby("building").resample("D")["kwh"].sum().reset_index()

    return daily


# ------------------------------------------------
# WEEKLY TOTALS
# ------------------------------------------------
def calculate_weekly_aggregates(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.dropna(subset=["timestamp"])
    df = df.set_index("timestamp")

    weekly = df.groupby("building").resample("W")["kwh"].sum().reset_index()

    return weekly


# ------------------------------------------------
# BUILDING SUMMARY
# ------------------------------------------------
def building_wise_summary(df):
    summary_df = df.groupby("building")["kwh"].agg(["mean", "min", "max", "sum"])
    summary_dict = summary_df.to_dict()
    return summary_df, summary_dict


