import streamlit as st
import pandas as pd
from src.experiment_analysis import load_experiments, get_best_experiment

st.set_page_config(page_title="ML Experiment Tracker", layout="wide")

st.title("ML Experiment Tracking Dashboard")

experiments = load_experiments()

if not experiments:
    st.warning("No experiments found.")
    st.stop()

df = pd.DataFrame(experiments)

df["rmse"] = df["metric"].apply(lambda x: x.get("rmse") if isinstance(x, dict) else None)


st.sidebar.header("Filters")

run_ids = df["run_id"].dropna().unique() if "run_id" in df.columns else []

selected_run = st.sidebar.selectbox(
    "Select Run ID",
    options=["All"] + list(run_ids)
)

if selected_run != "All":
    df = df[df["run_id"] == selected_run]


st.subheader("Experiments Table")
st.dataframe(df)


st.subheader("Best Experiment")

best = get_best_experiment(run_id=None if selected_run == "All" else selected_run)

if best:
    st.success(f"Best Model: {best['model']} | RMSE: {best['metric']['rmse']}")
    st.json(best)
else:
    st.warning("No valid experiment found.")

st.subheader("RMSE Comparison")

chart_df = df[["model", "rmse"]].dropna()

if not chart_df.empty:
    st.bar_chart(chart_df.set_index("model"))
else:
    st.info("No RMSE data available.")