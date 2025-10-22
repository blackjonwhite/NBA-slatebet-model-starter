# NBA Betting Model — Starter Kit

A minimal, practical scaffold to build an NBA betting model with Python.
Includes:
- Project structure for ETL, features, models, backtests, and a tiny Streamlit app
- Prefect flow for daily orchestration (local)
- MLflow tracking (optional, toggle in `.env`)
- Dockerfile + GitHub Actions CI lint

## Quickstart

```bash
# 1) Clone this repo (after you push it to GitHub)
git clone <YOUR_REPO_URL>.git
cd nba-betting-model-starter

# 2) Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3) Install dependencies
pip install -r requirements.txt

# 4) Copy env
cp .env.example .env

# 5) Run the demo pipeline
python -m nba_model.etl.daily_flow

# 6) Launch the minimal app
streamlit run src/nba_model/app/app.py
```

## What works now
- A demo ETL flow that creates a dummy "games" CSV and prints a model prediction placeholder.
- A simple feature pipeline stub.
- A Streamlit dashboard that shows today's (dummy) slate and "fair" lines.
- Backtest stub demonstrating walk-forward split API.

## Next steps
- Replace dummy ETL with real data sources.
- Implement real features and models (XGBoost/LogReg).
