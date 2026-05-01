import streamlit as st
import pandas as pd
from src.experiment_analysis import load_experiments, get_best_experiment
from src.predict import predict

st.set_page_config(page_title="ML Experiment Tracker", layout="wide")

st.title("ML Experiment Tracking Dashboard")

experiments = load_experiments()

if not experiments:
    st.warning("No experiments found.")
    st.stop()

df = pd.DataFrame(experiments)

df["rmse"] = df["metric"].apply(lambda x: x.get("rmse") if isinstance(x, dict) else None)


st.sidebar.header("🔍 Filters")

run_ids = df["run_id"].dropna().unique() if "run_id" in df.columns else []
selected_run = st.sidebar.selectbox("Select Run", ["All"] + list(run_ids))

if selected_run != "All":
    df = df[df["run_id"] == selected_run]


col1, col2 = st.columns([3, 2])

with col1:
    st.subheader("📊 Experiments")
    st.dataframe(df, use_container_width=True)


with col2:
    st.subheader("Best Model")

    best = get_best_experiment(run_id=None if selected_run == "All" else selected_run)

    if best:
        st.success(f"{best['model']} (RMSE: {best['metric']['rmse']:.4f})")
        st.json(best)
    else:
        st.warning("No valid model found")


st.subheader("Model Comparison")

chart_df = df[["model", "rmse"]].dropna()

if not chart_df.empty:
    st.bar_chart(chart_df.set_index("model"))
else:
    st.info("No RMSE data available")


st.subheader("Try Prediction")

feature1 = st.number_input("Feature 1", value=7)
feature2 = st.number_input("Feature 2", value=70)

if st.button("Predict"):
    input_df = pd.DataFrame({
        "feature1": [feature1],
        "feature2": [feature2]
    })

    preds = predict(input_df, run_id=None if selected_run == "All" else selected_run)

    if preds is not None:
        st.success(f"Prediction: {preds[0]}")