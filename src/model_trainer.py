from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

def train_models(x_train, y_train, x_test, y_test):
    models = {
        "LinearRegression": LinearRegression(),
        "DecisionTree": DecisionTreeRegressor(max_depth=5),
        "RandomForest": RandomForestRegressor(n_estimators=10)
    }

    results = []

    for name, model in models.items():
        model.fit(x_train, y_train)
        preds = model.predict(x_test)

        rmse = np.sqrt(mean_squared_error(y_test, preds))

        results.append({
            "model_name": name,
            "model": model,
            "rmse": rmse,
            "parameters": model.get_params()
        })

        print(f"Trained {name} | RMSE: {rmse}")

    return results