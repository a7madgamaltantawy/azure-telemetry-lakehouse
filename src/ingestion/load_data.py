import pandas as pd
import os

# Path setup
RAW_DATA_PATH = "data/raw"
FILE_NAME = "engine_data.csv"

def load_data():
    print("Loading dataset...")

    # Example dataset (temporary dummy data if not downloaded yet)
    data = {
        "unit_number": [1, 1, 1, 2, 2],
        "cycle": [1, 2, 3, 1, 2],
        "sensor_1": [100, 98, 95, 102, 99],
        "sensor_2": [200, 198, 190, 205, 202]
    }

    df = pd.DataFrame(data)

    # Ensure directory exists
    os.makedirs(RAW_DATA_PATH, exist_ok=True)

    file_path = os.path.join(RAW_DATA_PATH, FILE_NAME)

    df.to_csv(file_path, index=False)

    print(f"Data saved to {file_path}")

if __name__ == "__main__":
    load_data()