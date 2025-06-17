import pandas as pd
from sklearn.ensemble import IsolationForest

def compute_features(df):
    df = df.sort_values("date")
    df["returns"] = df["close"].pct_change()
    df["volatility"] = df["returns"].rolling(window=5).std()
    df["ma"] = df["close"].rolling(window=5).mean()
    df["delta"] = (df["close"] - df["ma"]) / df["ma"]
    return df.dropna()

def detect_anomalies(df, contamination=0.03):
    features = ["returns", "volatility", "delta"]
    df = df.dropna(subset=features).copy()
    iso = IsolationForest(contamination=contamination, random_state=42)
    df["anomaly_score"] = iso.fit_predict(df[features])
    df["is_anomaly"] = df["anomaly_score"] == -1
    return df
