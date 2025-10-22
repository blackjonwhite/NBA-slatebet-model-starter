import pandas as pd
from datetime import date

def walk_forward_split(df, split_date: str):
    train = df[df['date'] < split_date].copy()
    test = df[df['date'] >= split_date].copy()
    return train, test

if __name__ == "__main__":
    # Tiny demo with dummy dates
    df = pd.DataFrame({
        "date": ["2024-01-01","2024-02-01","2024-03-01"],
        "home_team": ["LAL","BOS","MIA"],
        "away_team": ["GSW","MIA","BOS"],
        "home_pts": [110, 103, 97],
        "away_pts": [105, 99, 101],
    })
    train, test = walk_forward_split(df, "2024-02-15")
    print("Train rows:", len(train), "Test rows:", len(test))
