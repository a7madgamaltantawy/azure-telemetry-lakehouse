import pandas as pd
import os

RAW_FILE_PATH = "data/raw/engine_data.csv"
PROCESSED_DIR = "data/processed"
PROCESSED_FILE_PATH = os.path.join(PROCESSED_DIR, "engine_data_processed.csv")


def transform_data():
    print("Reading raw telemetry data...")

    df = pd.read_csv(RAW_FILE_PATH)

    print(f"Input shape: {df.shape}")

    # Basic cleaning
    df = df.drop_duplicates()
    df = df.dropna()
    df = df.sort_values(by=["unit_number", "cycle"]).reset_index(drop=True)

    # Telemetry-style delta features
    df["sensor_2_delta"] = df.groupby("unit_number")["sensor_2"].diff().fillna(0)
    df["sensor_3_delta"] = df.groupby("unit_number")["sensor_3"].diff().fillna(0)
    df["sensor_4_delta"] = df.groupby("unit_number")["sensor_4"].diff().fillna(0)

    # Rolling averages (simple health trend signals)
    df["sensor_2_roll3"] = (
        df.groupby("unit_number")["sensor_2"]
        .rolling(window=3, min_periods=1)
        .mean()
        .reset_index(level=0, drop=True)
    )

    df["sensor_3_roll3"] = (
        df.groupby("unit_number")["sensor_3"]
        .rolling(window=3, min_periods=1)
        .mean()
        .reset_index(level=0, drop=True)
    )

    # Simple derived health indicator
    df["health_score"] = (
        df["sensor_2"].abs() +
        df["sensor_3"].abs() +
        df["sensor_4"].abs()
    ) / 3

    # Engine lifecycle indicator
    max_cycle_per_unit = df.groupby("unit_number")["cycle"].transform("max")
    df["cycle_ratio"] = df["cycle"] / max_cycle_per_unit

    os.makedirs(PROCESSED_DIR, exist_ok=True)
    df.to_csv(PROCESSED_FILE_PATH, index=False)

    print(f"Processed data saved to {PROCESSED_FILE_PATH}")
    print(f"Output shape: {df.shape}")
    print(df.head())


if __name__ == "__main__":
    transform_data()