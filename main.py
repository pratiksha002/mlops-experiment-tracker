import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from src.data_versioning import create_data_version
from src.experiment_tracker import log_experiment
from src.model_registry import save_model
import numpy as np

df = pd.DataFrame({
    "feature1": [1, 2, 3, 4, 5, 6],
    "feature2": [10, 20, 30, 40, 50, 60],
    "target": [100, 200, 300, 400, 500, 600]
})

data_version = create_data_version(df)

x = df.drop("target", axis=1)
y = df["target"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = RandomForestRegressor(n_estimators=10)
model.fit(x_train, y_train)

preds = model.predict(x_test)
rmse = np.sqrt(mean_squared_error(y_test, preds))

experiment_id = log_experiment({
    "model": "RandomForest",
    "parameters": {"n_estimators": 10},
    "metric": {"rmse": rmse},
    "data_version": data_version
})

model_path = save_model(model, "random_forest", experiment_id)
print("Model path:", model_path)
