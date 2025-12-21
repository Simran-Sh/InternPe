# 🏏 IPL Win Predictor Web App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg)](https://internpe-iplpredictiontool.streamlit.app/) 
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-orange)](https://scikit-learn.org/)

This repository contains an end‑to‑end **IPL Win Predictor** project, built as part of the **InternPe Data Science Internship – Project 3**. The application uses historical IPL ball-by-ball data to predict the winning probability of the chasing team in real-time.

**🔗 Live Demo:** [IPL Win Predictor Tool](https://internpe-iplpredictiontool.streamlit.app/)

---

## 🏏 Project Goal 🎯
The primary goal of this project is to train a ML Model and build an interactive web application that:
* Predicts the **win probability** of the batting team while chasing a target.
* Provides a simple UI to input live match conditions (teams, venue, target, score, overs, wickets).
* Returns winning chances for both teams based on historical patterns from 2008–2024


### Key Objectives:
* Preprocess and clean ball-by-ball IPL data.
* Engineer features like **Runs Left**, **Balls Left**, and **Required Run Rate**.
* Compare multiple ML models (Logistic Regression, SVC, Decision Trees, Random Forest).
* Deploy the final pipeline as a live web tool using Streamlit
  
---

## 📊 Dataset & Feature Engineering
The model was trained using Kaggle’s [IPL Complete Dataset](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020).

### Features Used for Prediction:
* **Categorical**: `batting_team`, `bowling_team`, `city`.
* **Numerical**: `runs_left`, `balls_left`, `wickets_left`, `total_runs_x` (target), `current_runrate`, `required_runrate`.

---

## 🤖 Model Comparison & Results
We implemented a `ColumnTransformer` to handle One-Hot Encoding and evaluated several classifiers:

| Model | Accuracy Score | Verdict |
| :--- | :--- | :--- |
| **Random Forest Classifier** | **99.86%** | **Selected ✅ (Robust & Generalizable)** |
| Decision Tree Classifier | 99.02% | High Accuracy (Potential Overfitting) |
| Logistic Regression | 81.02% | Reliable Baseline |
| SVC | 78.60% | Underperformed on this dataset |

The final model used is a **RandomForest** with 250 estimators, wrapped in a Scikit-Learn `Pipeline` for seamless deployment.

| Component | Description |
| :--- | :--- |
| **Preprocessing** | `OneHotEncoder` for categorical teams and cities. |
| **Model** | `RandomForestClassifier(n_estimators=250)`. |
| **Accuracy** | ~99% on test data (reflecting high historical pattern recognition). |
| **Serialization** | Pipeline saved as `ipl_model.pkl` (managed via Git LFS). |

---

### Feature Engineering (on app.py for Streamlit app)
To simulate a T20 chase, the following features were calculated from user input:
* **Runs Left**: Target − Current Score
* **Balls Left**: 120 − (Overs × 6)
* **Wickets Left**: 10 − Wickets Out
* **Current Run Rate (CRR)**: Current Score ÷ Overs Completed
* **Required Run Rate (RRR)**: (Runs Left × 6) ÷ Balls Left

---

## 🌐 How to Use the App
1.  **Select Teams**: Choose the Batting and Bowling teams.
2.  **Select Venue**: Choose the city where the match is played.
3.  **Enter Match Details**: Input the Target(Runs), Current Score, Overs Completed, and Wickets fallen.
4.  **Predict**: Click "Predict Probability" to see the win/loss percentage for both teams.

---

## 🚀 Installation & Local Usage
```bash
# 1. Clone the repository
git clone [https://github.com/Simran-Sh/InternPe.git](https://github.com/Simran-Sh/InternPe.git)

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
streamlit run app.py
