import joblib
from src.experiment_analysis import get_best_experiment

def load_best_model(run_id = None):
    best_exp = get_best_experiment(run_id=run_id)

    if best_exp is None:
        print("No valid experiment found.")

    model_path = best_exp["model_path"]
    print(f"Loading best model from: {model_path}")
    model = joblib.load(model_path)
    return model

def predict(input_data, run_id=None):
    model = load_best_model(run_id=run_id)

    if model is None:
        return None
    
    predictions = model.predict(input_data)
    print(f"Predictions: {predictions}")
    return predictions