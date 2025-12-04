import matplotlib.pyplot as plt
import pandas as pd
import os # <-- 1. Import the os module

# -----------------------------------------------------------
# Helper: Find peak-hour consumption (max kWh per building)
# -----------------------------------------------------------
def get_peak_hour_data(df):
    """
    Returns a DataFrame containing the highest kWh reading per building.
    """
    peak_rows = df.loc[df.groupby('building')['kwh'].idxmax()]
    return peak_rows


# -----------------------------------------------------------
# Dashboard plot function
# -----------------------------------------------------------
def create_dashboard(daily_df, weekly_df, df_combined, output_path="../output/dashboard.png"):
    """
    Creates a 3-panel visualization dashboard:
    1. Trend line (daily)
    2. Bar chart (weekly average per building)
    3. Scatter plot (peak-hour usage)
    Saves as dashboard.png
    """

    # Prepare peak-hour data
    peak_df = get_peak_hour_data(df_combined)

    # Create layout with 3 subplots
    fig, axs = plt.subplots(3, 1, figsize=(12, 15))
    fig.suptitle("Campus Energy Usage Dashboard", fontsize=16, fontweight='bold')

    # -----------------------------------------------------------
    # 1. DAILY TREND LINE
    # -----------------------------------------------------------
    for bname, group in daily_df.groupby("building"):
        axs[0].plot(group["timestamp"], group["kwh"], label=bname)

    axs[0].set_title("Daily Electricity Consumption")
    axs[0].set_xlabel("Date")
    axs[0].set_ylabel("kWh")
    axs[0].legend()
    axs[0].grid(True, linestyle='--', alpha=0.4)

    # -----------------------------------------------------------
    # 2. WEEKLY AVERAGE BAR CHART
    # -----------------------------------------------------------
    weekly_avg = weekly_df.groupby("building")["kwh"].mean()

    axs[1].bar(weekly_avg.index, weekly_avg.values)
    axs[1].set_title("Average Weekly Usage by Building")
    axs[1].set_ylabel("Average kWh")
    axs[1].grid(axis='y', linestyle='--', alpha=0.4)

    # -----------------------------------------------------------
    # 3. PEAK-HOUR SCATTER PLOT
    # -----------------------------------------------------------
    axs[2].scatter(peak_df["timestamp"], peak_df["kwh"])

    # Add building names next to points
    for _, row in peak_df.iterrows():
        axs[2].text(row["timestamp"], row["kwh"], row["building"], fontsize=9, ha="left")

    axs[2].set_title("Peak-Hour Electricity Consumption")
    axs[2].set_xlabel("Timestamp")
    axs[2].set_ylabel("kWh")
    axs[2].grid(True, linestyle='--', alpha=0.4)

    # Final layout adjustments
    plt.tight_layout(rect=[0, 0, 1, 0.96])  # make room for main title
    
    # -----------------------------------------------------------
    # ⭐ 2. FIX: Ensure output directory exists before saving ⭐
    # -----------------------------------------------------------
    output_dir = os.path.dirname(output_path)
    
    # Only try to create the directory if the path is not empty (i.e., not saving to current directory)
    if output_dir:
        # os.makedirs creates all intermediate directories needed.
        # exist_ok=True prevents an error if the directory already exists.
        os.makedirs(output_dir, exist_ok=True)
    # -----------------------------------------------------------

    plt.savefig(output_path, dpi=300)
    plt.close()

    print(f"Dashboard successfully saved to {output_path}")

