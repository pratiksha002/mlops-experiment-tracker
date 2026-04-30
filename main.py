import pandas as pd
from src.data_versioning import create_data_version
from src.experiment_tracker import log_experiment

df = pd.DataFrame({
    "feature1": [1, 2, 3, 4],
    "feature2": [10, 20, 30, 40],
    "target": [100, 200, 300, 400]
})

data_version = create_data_version(df)

experiment_id = log_experiment({
    "model": "RandomForest",
    "parameters": {"n_estimators": 100},
    "metric": {"rmse": 10.5},
    "data_version": data_version
})

print("Experiment ID:", experiment_id)
