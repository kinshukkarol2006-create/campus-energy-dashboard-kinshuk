from ingest import ingest_data
from aggregations import calculate_daily_totals, calculate_weekly_aggregates, building_wise_summary
from visualize import create_dashboard
from summary import export_cleaned_data, export_building_summary, generate_summary

print("\n=== Starting Capstone Pipeline ===")

# 1. INGEST DATA
df = ingest_data()
print("\n--- Loaded Data Columns ---")
print(df.columns)
print("----------------------------")

# Stop here if timestamp column missing
if "timestamp" not in df.columns:
    print("\n❌ ERROR: 'timestamp' column missing — check your CSV.")
    print("Columns found:", df.columns)
    exit()

# 2. AGGREGATIONS
print("\nRunning aggregations...")
daily_df = calculate_daily_totals(df)
weekly_df = calculate_weekly_aggregates(df)
summary_df, summary_dict = building_wise_summary(df)

# 3. VISUALIZATIONS
print("Creating dashboard...")
# --- FIX APPLIED HERE: Override the problematic default path with a local one.
create_dashboard(df, daily_df, weekly_df, output_path="./output/dashboard.png")

# 4. EXPORT SUMMARIES
print("Exporting cleaned data...")
export_cleaned_data(df)

print("Exporting building summary...")
export_building_summary(summary_df)

print("Generating executive summary...")
generate_summary(df, summary_df, daily_df, weekly_df)

print("\n🎉 All tasks completed successfully!")


