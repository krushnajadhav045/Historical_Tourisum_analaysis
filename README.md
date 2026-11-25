# Maharashtra Tourism Pattern & Multi-Prediction

A machine learning and Flask web application that analyzes tourism patterns across **Maharashtra, India** and predicts visitor crowd levels and visitor demographics from travel inputs.

## Overview

* **Web Application:** `app_3.py` (Flask app serving `templates/index.html`)
* **Training Notebook:** `Untitled.ipynb`
* **Dataset:** `tourism_maharashtra_pattern_dataset.csv`
* **Multi-Prediction Model Artifact:** `tourism_multi_prediction_model.pkl`
* **Single-Target Model Artifact (Notebook):** `tourism_model.pkl`

## Project Structure

```text
├── app_3.py                               # Flask web application for multi-target tourism predictions
├── Untitled.ipynb                           # Jupyter notebook for data exploration, training, and evaluation
├── tourism_maharashtra_pattern_dataset.csv  # Dataset of Maharashtra tourism attributes and patterns
├── tourism_multi_prediction_model.pkl       # Bundle containing (models, encoders, target_encoders) for app_3.py
├── tourism_model.pkl                      # Single-target RandomForest model saved in Untitled.ipynb
├── templates/
│   └── index.html                         # Frontend template rendered by app_3.py
└── README.md                              # Project documentation
```

## How the Flask App (`app_3.py`) Works

`app_3.py` loads `(models, encoders, target_encoders)` from `tourism_multi_prediction_model.pkl` and accepts form inputs from `/`:

* **Input Features:**
  * `Place` (e.g., *Ajanta Caves*, *Ellora Caves*, *Daulatabad Fort*, *Shani Shingnapur*, *Trimbakeshwar Temple*, *Gateway of India*, *Raigad Fort*, *Sindhudurg Fort*, *Mahabaleshwar*, *Shirdi*)
  * `Month` (*January* – *December*)
  * `Season` (*Winter*, *Summer*, *Monsoon*, *Post-Monsoon*)
  * `Weekend` (*Yes*, *No*)
* **Predicted Outputs:**
  * `Visitor_Count_Level` (Crowd level)
  * `Kids_Visitors`
  * `Senior_Citizens`
  * `Foreign_Tourists`

These decoded predictions are passed to `templates/index.html` as both `result` (dictionary) and `graph_data` (list).

## Getting Started

### 1. Install Dependencies

Install Python 3.9+ along with the required libraries:

```bash
pip install flask pandas numpy scikit-learn jupyter
```

### 2. Run the Flask Web App

Make sure `tourism_multi_prediction_model.pkl` and `templates/index.html` are in place, then start the server:

```bash
python app_3.py
```

By default, the app listens on `http://0.0.0.0:5000` (or the port specified in the `PORT` environment variable).

### 3. Explore or Retrain in Jupyter Notebook

Open `Untitled.ipynb` to inspect `tourism_maharashtra_pattern_dataset.csv` and train/evaluate models:

```bash
jupyter notebook Untitled.ipynb
```

## Notes & Schema Details

* **Notebook vs. Flask App Difference:** In the current `Untitled.ipynb` cells, a `RandomForestClassifier` (`n_estimators=200`, `random_state=42`) is trained on `["Month", "Season", "Weekend"]` to predict `Visitor_Count_Level` and saved as `tourism_model.pkl`, whereas `app_3.py` expects a tuple `(models, encoders, target_encoders)` in `tourism_multi_prediction_model.pkl` using four input features (`Place`, `Month`, `Season`, `Weekend`) and four target encoders (`Visitor_Count_Level`, `Kids_Visitors`, `Senior_Citizens`, `Foreign_Tourists`).
* **Environment Consistency:** Use compatible `scikit-learn`, `pandas`, and `numpy` versions when loading pickled artifacts so `LabelEncoder` and estimator objects unpickle cleanly.
* **Frontend Template:** Ensure `templates/index.html` handles `places`, `months`, `seasons`, `weekends`, `result`, and `graph_data` cleanly on both `GET` and `POST` requests.

## Author

**Krushna Jadhav** — MCA Department, Deogiri College, Chhatrapati Sambhajinagar
