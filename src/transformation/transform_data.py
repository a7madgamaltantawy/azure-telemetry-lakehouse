import pandas as pd
import os

RAW_FILE_PATH = "data/raw/engine_data.csv"
PROCESSED_DIR = "data/processed"
PROCESSED_FILE_PATH = os.path.join(PROCESSED_DIR, "engine_data_processed.csv")


def transform_data():
    print("Reading raw data...")

    df = pd.read_csv(RAW_FILE_PATH)

    print("Applying transformations...")

    # Remove duplicates
    df = df.drop_duplicates()

    # Check missing values
    df = df.dropna()

    # Sort data for consistency
    df = df.sort_values(by=["unit_number", "cycle"]).reset_index(drop=True)

    # Feature engineering
    df["sensor_1_delta"] = df.groupby("unit_number")["sensor_1"].diff().fillna(0)
    df["sensor_2_delta"] = df.groupby("unit_number")["sensor_2"].diff().fillna(0)

    # Simple health indicator example
    df["health_score"] = (df["sensor_1"] + df["sensor_2"]) / 2

    # Create processed directory if missing
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    # Save processed data
    df.to_csv(PROCESSED_FILE_PATH, index=False)

    print(f"Processed data saved to {PROCESSED_FILE_PATH}")
    print(df.head())


if __name__ == "__main__":
    transform_data()