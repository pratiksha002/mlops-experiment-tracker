import json
import os
from datetime import datetime
import uuid

log_file = "experiments/logs.json"

def log_experiment(experiment_data: dict) -> str:

    os.makedirs("experiments", exist_ok=True)

    experiment_id = f"exp_{uuid.uuid4().hex[:8]}"

    experiment_data["experiment_id"] = experiment_id
    experiment_data["timestamp"] = str(datetime.now())

    logs = []

    if os.path.exists(log_file):
        try:
            with open(log_file, "r") as f:
                content = f.read().strip()
                if content:
                    logs = json.loads(content)
                    if not isinstance(logs, list):
                        logs = []

        except Exception as e:
            print("Error reading logs:", e)
            logs = []

    logs.append(experiment_data)


    with open(log_file, "w") as f:
        json.dump(logs, f, indent=4)

    print(f"Experiment logged: {experiment_id}")

    return experiment_id