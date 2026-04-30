import json 
import os

log_file = "experiments/logs.json"

def load_experiments():
    if not os.path.exists(log_file):
        print("No experiments found")
        return []
    try:
        with open(log_file, "r") as f:
            data = json.load(f)

            if isinstance(data, list):
                return [exp for exp in data if isinstance(exp, dict)]
            else:
                return []

    except Exception as e:
        print("Error loading experiments:", e)
        return []
    

def get_best_experiment(metric_name="rmse"):
    experiments = load_experiments()

    print("DEBUG: experiments=", experiments)

    valid_experiments = [
        exp for exp in experiments
        if "metric" in exp
        and metric_name in exp["metric"]
        and "model_path" in exp
    ]

    if not valid_experiments:
        print("No valid experiments with model artifacts found.")
        return None

    best_exp = min(
        valid_experiments,
        key=lambda x: x["metric"][metric_name]
    )

    return best_exp


def print_best_experiment(metric_name="rmse"):
    best = get_best_experiment()

    if best is None:
        print("No experiments available.")
        return
    
    print("\nBEST EXPERIMENT")
    print("-" * 10)
    print(f"Experiment ID: {best['experiment_id']}")
    print(f"Model: {best['model']}")
    print(f"Params: {best['parameters']}")
    print(f"{metric_name.upper()}: {best['metric'][metric_name]}")
    print(f"Dataset Version: {best['data_version']}")
    print("-" * 10)


def update_experiment_with_model(experiment_id, model_path):
    import time
    
    time.sleep(0.1)

    experiments = load_experiments()
    updated = False

    for exp in experiments:
        if exp.get("experiment_id") == experiment_id:
            exp["model_path"] = model_path
            updated = True
            break

    with open(log_file, "w") as f:
        json.dump(experiments, f, indent=4)

    if updated:
        print(f"Updated experiment {experiment_id} with model path")
    else:
        print(f"Experiment {experiment_id} not found")