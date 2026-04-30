import joblib
from src.experiment_analysis import get_best_experiment

def load_best_model():
    best_exp = get_best_experiment()

    if best_exp is None:
        print("No valid experiment found.")

    model_path = best_exp["model_path"]
    print(f"Loading best model from: {model_path}")
    model = joblib.load(model_path)
    return model

def predict(input_data):
    model = load_best_model()

    if model is None:
        return None
    
    predictions = model.predict(input_data)
    print(f"Predictions: {predictions}")
    return predictions