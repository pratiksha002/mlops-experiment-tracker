# 🚀 ML Experiment Tracking System (Mini MLOps Platform)

An end-to-end machine learning experimentation platform that supports data versioning, experiment tracking, hyperparameter tuning, model registry, automated model selection, and an interactive dashboard for visualization and prediction.

---

## 🧠 Project Overview

This project simulates a real-world MLOps pipeline where multiple models are trained, evaluated, tracked, and deployed automatically.

It allows you to:

* Track experiments with metrics and parameters
* Perform hyperparameter tuning
* Store and version trained models
* Select the best model automatically
* Visualize results via a dashboard
* Run predictions using the best model

---

## ⚙️ Features

### 🔹 Data Versioning

* Generates a unique version ID for every dataset
* Ensures reproducibility

### 🔹 Experiment Tracking

* Logs model type, parameters, metrics (RMSE), and dataset version
* Stores experiments in a structured JSON format

### 🔹 Hyperparameter Tuning

* Implements manual grid search for Random Forest
* Evaluates multiple configurations and selects the best

### 🔹 Model Registry

* Saves trained models with versioned filenames
* Links models to corresponding experiments

### 🔹 Run-Based Experiment Grouping

* Groups experiments using `run_id`
* Ensures correct comparison within the same training session

### 🔹 Best Model Selection

* Automatically selects the best model based on RMSE
* Filters only valid experiments (with saved model artifacts)

### 🔹 Prediction System

* Loads the best model dynamically
* Generates predictions on new input data

### 🔹 Interactive Dashboard (Streamlit)

* Displays all experiments in a table
* Allows filtering by run_id
* Shows best model and performance
* Visualizes RMSE comparison
* Supports real-time predictions

---

## 🏗️ Project Structure

```
mlops-experiment-tracker/
│
├── src/
│   ├── data_versioning.py
│   ├── experiment_tracker.py
│   ├── model_registry.py
│   ├── experiment_analysis.py
│   ├── model_trainer.py
│   ├── predict.py
│
├── models/
│   └── saved_models/
│
├── experiments/
│   └── logs.json
│
├── app.py           # Streamlit dashboard
├── main.py          # Pipeline execution
└── README.md
```

---

## 🔄 Workflow

```
Dataset → Versioning → Model Training → Hyperparameter Tuning
        → Experiment Logging → Model Saving → Linking
        → Best Model Selection → Prediction → Visualization
```

---

## 📊 Example Output

* Trains multiple models (Linear Regression, Decision Tree, Random Forest)
* Selects best model based on RMSE
* Loads best model automatically
* Generates predictions

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone https://github.com/your-username/mlops-experiment-tracker.git
cd mlops-experiment-tracker
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run pipeline

```
python main.py
```

### 4. Launch dashboard

```
streamlit run app.py
```

---

## 🧠 Key Concepts Demonstrated

* MLOps fundamentals
* Experiment tracking systems
* Model lifecycle management
* Hyperparameter tuning
* Reproducibility
* Automated model selection
* Interactive ML dashboards

---

## 🔥 Future Improvements

* Add database (SQLite / PostgreSQL)
* Log all hyperparameter trials
* Add REST API (FastAPI)
* Deploy dashboard on cloud
* Add model performance tracking over time

---

## 💡 Inspiration

This project is inspired by real-world tools like:

* MLflow
* Weights & Biases

---


