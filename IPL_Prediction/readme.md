# 🏏 IPL Win Predictor Web App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg)](https://internpe-iplpredictiontool.streamlit.app/) 
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-orange)](https://scikit-learn.org/)

This repository contains an end‑to‑end **IPL Win Predictor** project, built as part of the **InternPe Data Science Internship – Project 3**. The application uses historical IPL ball-by-ball data to predict the winning probability of the chasing team in real-time.

**🔗 Live Demo:** [IPL Win Predictor Tool](https://internpe-iplpredictiontool.streamlit.app/)

---

## 🏏 Project Goal
The primary goal of this project is to build an interactive web application that:
* Predicts the **win probability** of the batting team while chasing a target.
* Provides a simple UI to input live match conditions (teams, venue, target, score, overs, wickets).
* Returns winning chances for both teams based on historical patterns.

---

## 📊 Dataset & Features
The model is trained on Kaggle’s [IPL Complete Dataset (2008–2020)](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020).

### Feature Engineering
To simulate a T20 chase, the following features were calculated from user input:
* **Runs Left**: Target − Current Score
* **Balls Left**: 120 − (Overs × 6)
* **Wickets Left**: 10 − Wickets Out
* **Current Run Rate (CRR)**: Current Score ÷ Overs Completed
* **Required Run Rate (RRR)**: (Runs Left × 6) ÷ Balls Left

---

## 🤖 Machine Learning Pipeline
Multiple models were evaluated, including Logistic Regression and SVC, but the **Random Forest Classifier** was selected for final deployment.

| Component | Description |
| :--- | :--- |
| **Preprocessing** | `OneHotEncoder` for categorical teams and cities. |
| **Model** | `RandomForestClassifier(n_estimators=250)`. |
| **Accuracy** | ~99% on test data (reflecting high historical pattern recognition). |
| **Serialization** | Pipeline saved as `ipl_model.pkl` (managed via Git LFS). |

---

## 🌐 How to Use the App
1.  **Select Teams**: Choose the Batting and Bowling teams.
2.  **Select Venue**: Choose the city where the match is played.
3.  **Enter Match Details**: Input the Target, Current Score, Overs Completed, and Wickets fallen.
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
