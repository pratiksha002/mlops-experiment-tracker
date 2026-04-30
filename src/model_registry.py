import os
import joblib
from datetime import datetime

model_path = "models/saved_models/"

def save_model(model, model_name: str, experiment_id: str) -> str:
    os.makedirs(model_path, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    model_version = f"{model_name}_{experiment_id}_{timestamp}"

    file_path = os.path.join(model_path, f"{model_version}.pkl")

    joblib.dump(model, file_path)

    print(f"Model saved: {model_version}")

    return file_path