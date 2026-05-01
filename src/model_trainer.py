from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
import itertools

def train_models(x_train, y_train, x_test, y_test):
    results = []

    lr = LinearRegression()
    lr.fit(x_train, y_train)
    preds = lr.predict(x_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))

    results.append({
        "model_name": "LinearRegression",
        "model": lr,
        "rmse": rmse,
        "parameters": lr.get_params()
    })

    print(f"LinearRegression | RMSE: {rmse}")


    dt = DecisionTreeRegressor(max_depth=5)
    dt.fit(x_train, y_train)
    preds = dt.predict(x_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))

    results.append({
        "model_name": "DecisionTree",
        "model": dt,
        "rmse": rmse,
        "parameters": dt.get_params()
    })

    print(f"DecisionTree | RMSE: {rmse}")


    param_grid = {
        "n_estimators": [10, 50],
        "max_depth": [None, 5]
    }

    best_model = None
    best_rmse = float("inf")
    best_params = None

    for n_estimators, max_depth in itertools.product(
        param_grid["n_estimators"],
        param_grid["max_depth"]
    ):
        rf = RandomForestRegressor(
            n_estimators=n_estimators,
            max_depth=max_depth
        )

        rf.fit(x_train, y_train)
        preds = rf.predict(x_test)

        rmse = np.sqrt(mean_squared_error(y_test, preds))

        print(f"RF | n={n_estimators}, depth={max_depth} → RMSE: {rmse}")

        if rmse < best_rmse:
            best_rmse = rmse
            best_model = rf
            best_params = {
                "n_estimators": n_estimators,
                "max_depth": max_depth
            }

    
    results.append({
        "model_name": "RandomForest",
        "model": best_model,
        "rmse": best_rmse,
        "parameters": best_params
    })

    print(f"Best RandomForest | RMSE: {best_rmse}")

    return results