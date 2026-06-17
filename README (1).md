# F1 AI/ML Analytics — Bahrain GP 2024

A professional **Flask + Plotly + Canvas** web application for Formula 1 race analytics, featuring live track animation, AI/ML predictions, anomaly detection, and interactive charts.

---

## Features
 
| Section | Details |
|---|---|
| **Track Animation** | Canvas-rendered Bahrain circuit with live car positions, lap counter, play/pause/scrub controls |
| **Race Leaderboard** | Real-time ranking sorted by average lap time, colour-coded by team |
| **KPI Strip** | Predicted winner, fastest lap, anomaly count, total data points |
| **Lap Time Evolution** | Plotly multi-driver chart with compound colouring and driver filter pills |
| **Tyre Compound** | Bar chart with error bars per compound (SOFT / MEDIUM / HARD) |
| **Sector Breakdown** | Grouped bar chart — Sector 1/2/3 for top 10 drivers |
| **AI Predictions** | Predicted ranking (RF model), confidence bars, feature importance bars |
| **Anomaly Detection** | Per-driver flagging (median + 2σ threshold), scatter chart of anomalous laps |

---

## Quick Start

```bash
# 1. Clone / navigate into the project
cd f1-aiml-analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Place your race_data.csv in the project root
#    (the app falls back to synthetic Bahrain GP 2024 data if absent)

# 4. Run
python web_app.py

# 5. Open http://localhost:5000
```

---

## Project Structure

```
f1-aiml-analysis/
├── web_app.py              ← Flask backend + all API routes
├── race_data.csv           ← Your FastF1 output (or synthetic fallback)
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html          ← Single-page HTML shell
│
├── static/
│   ├── css/style.css       ← F1 dark theme (Carbon + Speed Cyan palette)
│   └── js/script.js        ← All charts, animation, API calls
│
├── plots/                  ← Static PNG outputs (optional, from f1_analysis.py)
│
└── f1_cache/               ← FastF1 session cache
```

---

## API Endpoints

| Route | Returns |
|---|---|
| `GET /api/leaderboard` | Final race ranking, best/avg lap, gap |
| `GET /api/lap_times` | Per-driver lap number → time series |
| `GET /api/predictions` | Winner, fastest lap, ranking, feature importance |
| `GET /api/anomalies` | Per-driver anomaly lap list and counts |
| `GET /api/compound_stats` | Avg / median / std per tyre compound |
| `GET /api/sector_stats` | Avg S1/S2/S3 per driver (top 10) |
| `GET /api/race_summary` | Circuit meta, totals, fastest lap |

---

## CSV Column Requirements

The app uses these columns from `race_data.csv` (all optional — falls back gracefully):

| Column | Type | Notes |
|---|---|---|
| `Driver` | string | 3-letter abbreviation (VER, LEC…) |
| `DriverName` | string | Full name (optional) |
| `LapNumber` | int | 1-based |
| `LapTime` | float/timedelta | Seconds or `0 days HH:MM:SS.ffffff` |
| `Compound` | string | SOFT / MEDIUM / HARD |
| `TyreLife` | int | Laps on current set |
| `Sector1Time` / `Sector2Time` / `Sector3Time` | float | Seconds |
| `SpeedST` / `SpeedI1` / `SpeedI2` / `SpeedFL` | float | km/h |
| `IsAnomaly` | bool | Pre-flagged (or computed automatically) |

---

## Production Deployment

```bash
gunicorn -w 4 -b 0.0.0.0:8000 web_app:app
```

---

## Tech Stack

- **Backend**: Flask 3, pandas, NumPy, scikit-learn
- **Data**: FastF1 API → Bahrain GP 2024
- **Charts**: Plotly.js (interactive, hover, zoom)
- **Animation**: HTML5 Canvas
- **Fonts**: Orbitron (display) + Inter (body)
- **Theme**: Carbon dark palette, F1 red accent, Speed Cyan data colour
