import pandas as pd
from pathlib import Path
import logging
import os

# ------------------------------------------------
# Logging configuration
# ------------------------------------------------
os.makedirs("output", exist_ok=True)

logging.basicConfig(
    filename="output/ingestion.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ------------------------------------------------
# Ingest Function
# ------------------------------------------------
def ingest_data():
    data_dir = Path("data")
    csv_files = list(data_dir.glob("*.csv"))

    if not csv_files:
        logging.error("No CSV files found in /data/")
        raise FileNotFoundError("No CSV files found in /data/")

    df_list = []

    for file in csv_files:
        try:
            logging.info(f"Reading file: {file}")

            temp = pd.read_csv(
                file,
                encoding="utf-8-sig",
                on_bad_lines="skip"
            )

            # Clean column names
            temp.columns = (
                temp.columns.str.strip()
                              .str.replace("\ufeff", "", regex=False)
            )

            # Convert timestamp to datetime
            temp["timestamp"] = pd.to_datetime(temp["timestamp"], errors="coerce")

            # Add metadata
            temp["building"] = file.stem.split("_")[0]
            temp["month"] = file.stem.split("_")[1]

            df_list.append(temp)

        except Exception as e:
            logging.error(f"Error reading {file}: {e}")

    df = pd.concat(df_list, ignore_index=True)

    # Final check: ensure timestamp is datetime for entire df
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    return df



