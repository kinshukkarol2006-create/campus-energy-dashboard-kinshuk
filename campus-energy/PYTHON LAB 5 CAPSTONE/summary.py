import pandas as pd
import os # <-- 1. Import os for directory operations
# You may need other imports here depending on your original file

# Helper function to ensure directory exists for exporting
def ensure_dir(filepath):
    """Checks if the parent directory of a file exists and creates it if not."""
    output_dir = os.path.dirname(filepath)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

# -----------------------------------------------------------
# Export Cleaned Data (The function causing the current error)
# -----------------------------------------------------------
def export_cleaned_data(df, output_path="./output/cleaned_data.csv"):
    """Exports the cleaned DataFrame to a CSV file."""
    
    # ⭐ FIX: Ensure the output directory exists before Pandas tries to write
    ensure_dir(output_path)
    
    df.to_csv(output_path, index=False)
    print(f"Cleaned data successfully exported to {output_path}")

# -----------------------------------------------------------
# Export Building Summary (Proactively fixed, as it is the next line)
# -----------------------------------------------------------
def export_building_summary(summary_df, output_path="./output/building_summary.csv"):
    """Exports the building summary DataFrame to a CSV file."""
    
    # ⭐ FIX: Ensure the output directory exists before Pandas tries to write
    ensure_dir(output_path)
    
    summary_df.to_csv(output_path)
    print(f"Building summary successfully exported to {output_path}")

# -----------------------------------------------------------
# Placeholder for generate_summary
# -----------------------------------------------------------
def generate_summary(df, summary_df, daily_df, weekly_df):
    # If this function exports a file, it will also need the ensure_dir() call.
    # For now, we will assume it prints the summary to console.
    print("Executive summary generated (to console/log, implementation pending).")
    # Example: print(f"Total kWh recorded: {df['kwh'].sum()}")

    # If this function exports a file, add:
    # ensure_dir(output_path)
    # with appropriate output_path
    pass


