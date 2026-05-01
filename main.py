import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from src.data_versioning import create_data_version
from src.experiment_tracker import log_experiment
from src.model_registry import save_model
import numpy as np
from src.experiment_analysis import print_best_experiment
from src.experiment_analysis import update_experiment_with_model
from src.predict import predict
from src.model_trainer import train_models

df = pd.DataFrame({
    "feature1": [1, 2, 3, 4, 5, 6],
    "feature2": [10, 20, 30, 40, 50, 60],
    "target": [100, 200, 300, 400, 500, 600]
})

data_version = create_data_version(df)

x = df.drop("target", axis=1)
y = df["target"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

results = train_models(x_train, y_train, x_test, y_test)

for result in results:
    model = result["model"]
    model_name = result["model_name"]
    rmse = result["rmse"]
    params = result["parameters"]

    experiment_id = log_experiment({
        "model": model_name,
        "parameters": params,
        "metric": {"rmse": rmse},
        "data_version": data_version
    })

    model_path = save_model(model, model_name.lower(), experiment_id)

    update_experiment_with_model(experiment_id, model_path)
    print(f"Model saved for {model_name}: {model_path}")

print_best_experiment()

test_input = pd.DataFrame({

    "feature1": [7, 8],
    "feature2": [70, 80]
})

predict(test_input)