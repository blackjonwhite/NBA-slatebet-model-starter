"""Demo daily flow using Prefect-like structure (pure Python for simplicity)."""
import os
import pandas as pd
from datetime import datetime
from pathlib import Path

from nba_model.utils.common import RAW_DIR, PROC_DIR

def make_dummy_games():
    today = datetime.today().date()
    df = pd.DataFrame([
        {"date": str(today), "home_team": "LAL", "away_team": "GSW", "close_spread": -3.5, "close_total": 231.5},
        {"date": str(today), "home_team": "BOS", "away_team": "MIA", "close_spread": -6.0, "close_total": 220.5},
    ])
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    path = RAW_DIR / f"games_{today}.csv"
    df.to_csv(path, index=False)
    print(f"Wrote dummy games to {path}")
    return path

def build_features(games_csv: Path):
    df = pd.read_csv(games_csv)
    # Very naive features
    df["elo_home"] = 1600.0
    df["elo_away"] = 1600.0
    df["elo_diff"] = df["elo_home"] - df["elo_away"]
    out = PROC_DIR / "features_today.csv"
    df.to_csv(out, index=False)
    print(f"Built features -> {out}")
    return out

def predict(features_csv: Path):
    df = pd.read_csv(features_csv)
    # Placeholder: predict fair spread as -elo_diff/25 and fair total as close_total (no change)
    df["fair_spread"] = -df["elo_diff"]/25.0
    df["fair_total"] = df["close_total"]
    out = PROC_DIR / "predictions_today.csv"
    df.to_csv(out, index=False)
    print(f"Predictions saved -> {out}")
    return out

if __name__ == "__main__":
    games = make_dummy_games()
    feats = build_features(games)
    preds = predict(feats)
    print("Daily flow completed.")
