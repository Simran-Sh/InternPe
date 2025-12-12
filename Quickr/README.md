# InternPe
AI / ML Internship from InternPe


🚗 Vehicle Price Prediction — AI/ML Internship Project (InternPe)

This project focuses on building a regression model to predict used vehicle prices using Python, machine learning, and a fully cleaned dataset.

The workflow includes data ingestion, preprocessing, feature engineering, and model training.

🧰 Tools & Technologies Used
Python 3.x
Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn
VS Code with Jupyter Extension
Jupyter Notebook Environment
GitHub for version control

📂 Project Workflow
1️⃣ Import Libraries
Essential libraries such as pandas, numpy, matplotlib, seaborn, and sklearn were imported to support data cleaning and model development.

2️⃣ Load the Dataset
The dataset (CSV file) containing used vehicle information was loaded using pandas.read_csv().

3️⃣ Build the Regressor
A machine learning regressor was created to predict car prices based on cleaned and preprocessed features.

🧼 Data Cleaning and Preprocessing
The initial dataset contained significant inconsistencies and unusable values which required extensive cleaning before model training. The goal of this phase was to create a high-quality, reliable dataset for training the vehicle price prediction model.

📝 Key Observations and Quality Issues
The raw dataset, comprising 892 rows and 6 columns, contained several quality issues in critical features:

| Column         | Issue Details                       | Examples                                 |
| -------------- | ----------------------------------- | ---------------------------------------- |
| **price**      | Strings, commas, non-numeric values | `'Ask For Price'`, `'4,25,000'`          |
| **year**       | Irrelevant text, incorrect formats  | `'...'`, `'Zest'`, `'2007'`              |
| **kms_driven** | Units, commas, invalid text, NaNs   | `'45,000 kms'`, `'Petrol'`, `NaN`        |
| **fuel_type**  | Missing values                      | `NaN`                                    |
| **name**       | Very high cardinality               | `'Hyundai Santro Xing XO eRLX Euro III'` |


🛠️ Step-by-Step Cleaning Strategy
We employed a row-wise removal strategy for corrupted entries, as these samples contained insufficient information to be useful for the prediction model

| Step  | Column     | Cleaning Operation                                                              | Final Type |
| ----- | ---------- | ------------------------------------------------------------------------------- | ---------- |
| **1** | price      | Removed `'Ask For Price'`, stripped commas, converted to numeric                | `int`      |
| **2** | year       | Removed text, kept only 4-digit years, restricted range to 1990–2025            | `int`      |
| **3** | kms_driven | Removed NaNs, stripped `' kms'`, removed commas & non-digits, validated numeric | `int`      |
| **4** | fuel_type  | Dropped rows with missing values                                                | `object`   |
| **5** | name       | Standardized names by keeping first **three words**                             | `object`   |


📈 Cleaning Summary
The rigorous cleaning process significantly improved data quality, resulting in a robust dataset suitable for model training:

| Metric               | Before Cleaning      | After Cleaning |
| -------------------- | -------------------- | -------------- |
| **Dataset Size**     | 892 rows             | ~816 rows      |
| **Rows Dropped**     | —                    | ~8%            |
| **price dtype**      | Mixed / object       | Clean `int`    |
| **kms_driven dtype** | Mixed / object       | Clean `int`    |
| **Missing Values**   | Present in 3 columns | Removed        |


The final cleaned dataset, is now ready for Feature Engineering and Model Training

