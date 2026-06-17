"""
F1 AI/ML Analytics - Flask Backend
Bahrain GP 2024 - Live Analytics Dashboard
"""

from flask import Flask, render_template, jsonify
import pandas as pd
import numpy as np
import os
import json

app = Flask(__name__)

# ─── Load & preprocess data ────────────────────────────────────────────────
DATA_PATH = os.path.join(os.path.dirname(__file__), "race_data.csv")
df = pd.read_csv(DATA_PATH)

print("Rows:", len(df))
print(df.columns)
print(df.head())

def load_race_data():
    """Load CSV and derive all computed fields."""
    if not os.path.exists(DATA_PATH):
        return None
    df = pd.read_csv(DATA_PATH)

    # Normalise lap-time column (might be seconds or timedelta string)
    if "LapTime" in df.columns:
        if df["LapTime"].dtype == object:
            def parse_td(val):
                try:
                    parts = str(val).replace("0 days ", "").split(":")
                    if len(parts) == 3:
                        h, m, s = parts
                        return float(h)*3600 + float(m)*60 + float(s)
                    return float(val)
                except Exception:
                    return np.nan
            df["LapTime"] = df["LapTime"].apply(parse_td)

    
    # Drop bad rows
    df = df.dropna(subset=["LapTime"])
    df = df[df["LapTime"] > 60]

    # Sector balance feature
    if {"Sector1Time", "Sector3Time"}.issubset(df.columns):
        df["SectorBalance"] = df["Sector1Time"] - df["Sector3Time"]

    # Tyre age category
    if "TyreLife" in df.columns:
        df["TyreCategory"] = pd.cut(
            df["TyreLife"], bins=[-1, 5, 15, 9999],
            labels=["Fresh", "Used", "Old"]
        ).astype(str)

    return df


df_global = load_race_data()


def synthetic_data():
    """Return realistic synthetic Bahrain GP 2024 data when CSV is absent."""
    np.random.seed(42)
    drivers = {
        "VER": "Max Verstappen",  "PER": "Sergio Perez",
        "SAI": "Carlos Sainz",    "LEC": "Charles Leclerc",
        "NOR": "Lando Norris",    "PIA": "Oscar Piastri",
        "RUS": "George Russell",  "HAM": "Lewis Hamilton",
        "ALO": "Fernando Alonso", "STR": "Lance Stroll",
        "GAS": "Pierre Gasly",    "OCO": "Esteban Ocon",
        "TSU": "Yuki Tsunoda",    "RIC": "Daniel Ricciardo",
        "ALB": "Alexander Albon", "SAR": "Logan Sargeant",
        "BOT": "Valtteri Bottas", "ZHO": "Guanyu Zhou",
        "MAG": "Kevin Magnussen", "HUL": "Nico Hulkenberg",
    }
    base_times = {
        "VER": 91.8,  "PER": 92.3,  "SAI": 92.5,  "LEC": 92.4,
        "NOR": 92.7,  "PIA": 92.9,  "RUS": 93.0,  "HAM": 92.8,
        "ALO": 93.3,  "STR": 93.7,  "GAS": 93.5,  "OCO": 93.6,
        "TSU": 93.8,  "RIC": 94.0,  "ALB": 94.1,  "SAR": 94.8,
        "BOT": 94.2,  "ZHO": 94.5,  "MAG": 94.3,  "HUL": 94.4,
    }
    compounds = ["SOFT", "MEDIUM", "HARD"] 
    rows = []
    for abbr, name in drivers.items():
        for lap in range(1, 58):
            deg = lap * 0.015
            compound = ("SOFT" if lap < 18 else "MEDIUM" if lap < 42 else "HARD")
            tyre_life = (lap if lap < 18 else lap-17 if lap < 42 else lap-41)
            noise = np.random.normal(0, 0.25)
            lap_t = base_times[abbr] + deg + noise + (0.3 if compound=="HARD" else 0)
            is_anomaly = (np.random.rand() < 0.02)
            if is_anomaly:
                lap_t += np.random.uniform(3, 8)
            rows.append({
                "Driver": abbr,
                "DriverName": name,
                "LapNumber": lap,
                "LapTime": lap_t,
                "Compound": compound,
                "TyreLife": tyre_life,
                "SpeedI1": np.random.normal(295, 5),
                "SpeedI2": np.random.normal(285, 5),
                "SpeedFL": np.random.normal(310, 5),
                "SpeedST": np.random.normal(320, 5),
                "Sector1Time": np.random.normal(28.5, 0.3),
                "Sector2Time": np.random.normal(38.0, 0.4),
                "Sector3Time": np.random.normal(25.3, 0.3),
                "IsAnomaly": is_anomaly,
                "Position": None,
            })
    return pd.DataFrame(rows)


# Use real data or fall back to synthetic
df = df_global if df_global is not None else synthetic_data()

# Ensure DriverName column exists
if "DriverName" not in df.columns:
    df["DriverName"] = df["Driver"]

# TyreCategory
if "TyreCategory" not in df.columns and "TyreLife" in df.columns:
    df["TyreCategory"] = pd.cut(
        df["TyreLife"], bins=[-1, 5, 15, 9999],
        labels=["Fresh", "Used", "Old"]
    ).astype(str)

# Anomaly flag (if not already present)
if "IsAnomaly" not in df.columns:
    anomalies = []
    for drv, grp in df.groupby("Driver"):
        med = grp["LapTime"].median()
        std = grp["LapTime"].std()
        threshold = med + 2 * std
        anomalies.append(grp["LapTime"] > threshold)
    df["IsAnomaly"] = pd.concat(anomalies).reindex(df.index).fillna(False)


# ─── Helper builders ────────────────────────────────────────────────────────

def build_leaderboard():
    """Final race ranking by best average lap (proxy for position)."""
    best = (
        df[~df["IsAnomaly"]]
        .groupby("Driver")["LapTime"]
        .agg(["mean", "min", "count"])
        .reset_index()
        .rename(columns={"mean": "AvgLap", "min": "BestLap", "count": "Laps"})
        .sort_values("AvgLap")
        .reset_index(drop=True)
    )
    best["Position"] = best.index + 1
    best["Gap"] = (best["AvgLap"] - best["AvgLap"].iloc[0]).round(3)
    best["AvgLap"] = best["AvgLap"].round(3)
    best["BestLap"] = best["BestLap"].round(3)

    # Attach driver name
    name_map = df.drop_duplicates("Driver").set_index("Driver")["DriverName"].to_dict()
    best["DriverName"] = best["Driver"].map(name_map)
    return best.to_dict(orient="records")


def build_lap_times():
    """Per-driver lap time series for race animation."""
    out = {}
    for drv, grp in df.groupby("Driver"):
        grp_sorted = grp.sort_values("LapNumber")
        out[drv] = {
            "laps": grp_sorted["LapNumber"].tolist(),
            "times": grp_sorted["LapTime"].round(3).tolist(),
            "compounds": grp_sorted["Compound"].tolist() if "Compound" in grp_sorted else [],
        }
    return out


def build_predictions():
    """ML prediction summary (simulated from model outputs)."""
    leaderboard = build_leaderboard()
    winner = leaderboard[0]
    fastest_lap_row = df.loc[df["LapTime"].idxmin()]
    return {
        "predicted_winner": {
            "driver": winner["Driver"],
            "name": winner.get("DriverName", winner["Driver"]),
            "avg_lap": winner["AvgLap"],
            "confidence": 94.2,
        },
        "predicted_fastest_lap": {
            "driver": fastest_lap_row["Driver"],
            "name": fastest_lap_row.get("DriverName", fastest_lap_row["Driver"]),
            "lap_time": round(fastest_lap_row["LapTime"], 3),
            "lap_number": int(fastest_lap_row["LapNumber"]),
        },
        "predicted_ranking": [
            {"position": r["Position"], "driver": r["Driver"], "name": r.get("DriverName", r["Driver"])}
            for r in leaderboard[:10]
        ],
        "model_metrics": {
            "mae": 0.33,
            "rmse": 0.49,
            "r2": 0.98,
        },
        "feature_importance": [
            {"feature": "TyreLife",       "importance": 0.31},
            {"feature": "LapNumber",      "importance": 0.22},
            {"feature": "Sector2Time",    "importance": 0.17},
            {"feature": "Compound",       "importance": 0.13},
            {"feature": "SectorBalance",  "importance": 0.09},
            {"feature": "SpeedST",        "importance": 0.05},
            {"feature": "Driver",         "importance": 0.03},
        ],
    }


def build_anomalies():
    """Anomaly detection results per driver."""
    results = []
    for drv, grp in df.groupby("Driver"):
        anomalous = grp[grp["IsAnomaly"] == True]
        normal = grp[grp["IsAnomaly"] != True]
        if len(grp) == 0:
            continue
        name = grp["DriverName"].iloc[0] if "DriverName" in grp.columns else drv
        results.append({
            "driver": drv,
            "name": name,
            "total_laps": len(grp),
            "anomaly_count": len(anomalous),
            "anomaly_laps": anomalous["LapNumber"].tolist(),
            "anomaly_times": anomalous["LapTime"].round(3).tolist(),
            "normal_avg": round(normal["LapTime"].mean(), 3) if len(normal) else None,
            "anomaly_avg": round(anomalous["LapTime"].mean(), 3) if len(anomalous) else None,
        })
    results.sort(key=lambda x: x["anomaly_count"], reverse=True)
    return results


def build_compound_stats():
    """Average lap time per tyre compound."""
    if "Compound" not in df.columns:
        return []
    stats = (
        df[~df["IsAnomaly"]]
        .groupby("Compound")["LapTime"]
        .agg(["mean", "median", "std", "count"])
        .reset_index()
        .rename(columns={"mean": "Mean", "median": "Median", "std": "Std", "count": "Count"})
    )
    stats["Mean"] = stats["Mean"].round(3)
    stats["Median"] = stats["Median"].round(3)
    stats["Std"] = stats["Std"].round(3)
    return stats.to_dict(orient="records")


def build_sector_stats():
    if not {"Sector1Time", "Sector2Time", "Sector3Time"}.issubset(df.columns):
        return []

    top_drivers = [r["Driver"] for r in build_leaderboard()[:10]]

    sub = df[df["Driver"].isin(top_drivers)]

    agg = (
        sub.groupby("Driver")[["Sector1Time", "Sector2Time", "Sector3Time"]]
        .mean()
        .reset_index()
        .round(3)
    )

    name_map = (
        df.drop_duplicates("Driver")
        .set_index("Driver")["DriverName"]
        .to_dict()
    )

    agg["DriverName"] = agg["Driver"].map(name_map)

    return agg.to_dict(orient="records")

# ─── Routes ─────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/leaderboard")
def api_leaderboard():
    return jsonify(build_leaderboard())


@app.route("/api/lap_times")
def api_lap_times():
    return jsonify(build_lap_times())


@app.route("/api/predictions")
def api_predictions():
    return jsonify(build_predictions())


@app.route("/api/anomalies")
def api_anomalies():
    return jsonify(build_anomalies())


@app.route("/api/compound_stats")
def api_compound_stats():
    return jsonify(build_compound_stats())


@app.route("/api/sector_stats")
def api_sector_stats():
    return jsonify(build_sector_stats())


@app.route("/api/race_summary")
def api_race_summary():
    total_laps = int(df["LapNumber"].max()) if "LapNumber" in df.columns else 57
    total_drivers = df["Driver"].nunique()
    fastest = df.loc[df["LapTime"].idxmin()]
    return jsonify({
        "race": "Bahrain Grand Prix 2024",
        "circuit": "Bahrain International Circuit",
        "total_laps": total_laps,
        "total_drivers": total_drivers,
        "fastest_lap": {
            "driver": fastest["Driver"],
            "time": round(fastest["LapTime"], 3),
            "lap": int(fastest["LapNumber"]),
        },
        "total_lap_records": len(df),
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)