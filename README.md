#  SmartAgroAI

An AI-powered smart agriculture assistant that predicts **annual rainfall** and recommends the **best crop** based on soil and weather inputs. Built with a Python Flask backend and a lightweight HTML frontend.

---

##  Features

-  **Rainfall Prediction** — Predicts annual rainfall from monsoon month data (Jun–Sep)
-  **Crop Recommendation** — Recommends the most suitable crop based on soil nutrients, temperature, humidity, pH, and rainfall
-  **Prediction Logging** — Saves every prediction to a CSV log file
-  **REST API** — Flask backend with CORS support for frontend integration

---

## 🧠 ML Models

### Rainfall Prediction (Regression)
Models evaluated on historical Indian rainfall data:

| Model | Type |
|-------|------|
| Linear Regression | Baseline |
| Decision Tree Regressor | Tree-based |
| Random Forest Regressor | Ensemble |
| Gradient Boosting Regressor | Boosting |

**Input features:** `JUN`, `JUL`, `AUG`, `SEP` (monthly rainfall in mm)  
**Output:** Predicted annual rainfall (mm)

---

### Crop Recommendation (Classification)
Models evaluated on soil & weather dataset:

| Model | Type |
|-------|------|
| K-Nearest Neighbors | Instance-based |
| Support Vector Machine | Kernel-based |
| Decision Tree | Tree-based |
| Random Forest | Ensemble |

**Input features:** `N`, `P`, `K`, `Temperature`, `Humidity`, `pH`, `Rainfall`  
**Output:** Recommended crop label (e.g., rice, maize, banana...)

---

## 🗂️ Project Structure

```
SmartAgroAI/
├── api/
│   ├── app.py              # Flask app entry point
│   ├── routes.py           # API route definitions
│   └── __init__.py
├── data/
│   ├── raw/
│   │   ├── crop_recommendation.csv
│   │   └── rainfall.csv
│   └── processed/
│       ├── crop_clean.csv
│       └── rainfall_clean.csv
├── frontend/
│   └── index.html          # Web UI
├── models/
│   ├── crop_model.pkl      # Trained crop model
│   └── rainfall_model.pkl  # Trained rainfall model
├── notebooks/
│   ├── crop_analysis.ipynb
│   └── rainfall_analysis.ipynb
├── outputs/
│   └── predictions_log.csv
├── src/
│   ├── prediction/
│   │   ├── crop_predictor.py
│   │   └── rainfall_predictor.py
│   ├── preprocessing/
│   │   ├── clean_crop.py
│   │   ├── clean_rainfall.py
│   │   └── feature_engineering.py
│   └── training/
│       ├── crop.py
│       ├── rainfall.py
│       ├── train_crop.py
│       └── train_rainfall.py
├── requirements.txt
├── Procfile
└── README.md
```

---

## Example Input Values

| Parameter | Rice | Maize | Banana |
|-----------|------|-------|--------|
| Nitrogen (N) | 90 | 77 | 105 |
| Phosphorus (P) | 42 | 52 | 35 |
| Potassium (K) | 43 | 75 | 50 |
| Temperature (°C) | 21 | 23 | 27 |
| Humidity (%) | 82 | 65 | 80 |
| Soil pH | 6.5 | 6.2 | 6.0 |
| Rainfall (mm) | 203 | 195 | 120 |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask, Flask-CORS |
| ML | scikit-learn, XGBoost, joblib |
| Data | pandas, numpy |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Render (backend), Vercel (frontend) |

---
