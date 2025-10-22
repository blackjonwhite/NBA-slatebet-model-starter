import streamlit as st
import pandas as pd
from pathlib import Path
from nba_model.utils.common import RAW_DIR, PROC_DIR

st.set_page_config(page_title="NBA Model — Starter", layout="centered")

st.title("NBA Betting Model — Starter App")

preds_path = PROC_DIR / "predictions_today.csv"
if preds_path.exists():
    df = pd.read_csv(preds_path)
    st.subheader("Today's Slate (Demo)")
    st.dataframe(df)
else:
    st.info("Run the daily flow first to generate today's predictions.")
