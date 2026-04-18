import pandas as pd
import os

RAW_PATH = "data/raw"
INPUT_FILE = os.path.join(RAW_PATH, "train_FD001.txt")  # أو الاسم الجديد
OUTPUT_FILE = os.path.join(RAW_PATH, "engine_data.csv")

COLUMNS = [
    "unit_number", "cycle",
    "setting_1", "setting_2", "setting_3",
    *[f"sensor_{i}" for i in range(1, 22)]
]

def load_data():
    print("Loading telemetry-style engine data...")

    df = pd.read_csv(
        INPUT_FILE,
        sep=r"\s+",
        header=None,
        engine="python"
    )

    # remove empty columns لو موجودة
    df = df.dropna(axis=1, how="all")

    print(f"Raw shape: {df.shape}")

    df.columns = COLUMNS

    # ترتيب مهم (telemetry style)
    df = df.sort_values(by=["unit_number", "cycle"])

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved to: {OUTPUT_FILE}")
    print(df.head())

if __name__ == "__main__":
    load_data()