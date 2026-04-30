import os
import hashlib
import pandas as pd
import json
from datetime import datetime

data_version_path = "data/versions/"

def generate_hash(df: pd.DataFrame) -> str:

    df_bytes = df.to_csv(index=False).encode()
    return hashlib.md5(df_bytes).hexdigest()

def create_data_version(df: pd.DataFrame, dataset_name="dataset") -> str:
    os.makedirs(data_version_path, exist_ok=True)

    data_hash = generate_hash(df)

    version_id = f"{dataset_name}_{data_hash[:6]}"

    file_path = os.path.join(data_version_path, f"{version_id}.csv")
    df.to_csv(file_path, index=False)

    metadata = {
        "version_id": version_id,
        "dataset_name": dataset_name,
        "rows": df.shape[0],
        "columns": df.shape[1],
        "hash": data_hash,
        "created_at": str(datetime.now())
    }

    metadata_path = file_path.replace(".csv", ".json")

    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=4)

    print(f"Data version created: {version_id}")

    return version_id