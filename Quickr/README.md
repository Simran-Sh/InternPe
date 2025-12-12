# InternPe
AI / ML Internship from InternPe


Workflow 

import libraries 
import csv dataset 
Create Regressor to predit price






🧼 Data Cleaning and Preprocessing
The initial dataset contained significant inconsistencies and unusable values which required extensive cleaning before model training. The goal of this phase was to create a high-quality, reliable dataset for training the vehicle price prediction model.

📝 Key Observations and Quality Issues
The raw dataset, comprising 892 rows and 6 columns, contained several quality issues in critical features:

Column,Initial Issue,Example of Bad Data
Price,"Contains strings, commas, and non-numeric values.","'Ask For Price', '4,25,000'"
year,Contains irrelevant text and incorrect formats.,"'...', 'Zest', '2007' (as object)"
kms_driven,"Contains units, commas, non-numeric values, and NaNs.","'45,000 kms', 'Petrol', NaN"
fuel_type,Contains Missing Values (NaN).,NaN
name,High cardinality (too many unique values).,'Hyundai Santro Xing XO eRLX Euro III'

🛠️ Step-by-Step Cleaning Strategy
We employed a row-wise removal strategy for corrupted entries, as these samples contained insufficient information to be useful for the prediction model.
Step,Column,Cleaning Operation,Resulting Data Type
1.,Price,"Filtered out 'Ask For Price' entries, removed commas (,), and converted the column to the integer data type.",int
2.,year,"Filtered out all non-4-digit strings (e.g., 'Zest', 'TOUR') using Regular Expressions, and converted the column to the integer data type. A logical filter was applied to restrict years between 1990 and 2025.",int
3.,kms_driven,"Dropped rows with NaN values, stripped the ' kms' unit and commas (,), and filtered out any rows that still contained non-digit characters, ensuring only valid mileage data remained. Converted to integer.",int
4.,fuel_type,Dropped all rows containing missing values (NaN).,object
5.,name,"Reduced the high cardinality by standardizing the entries. Each car name was truncated to include only the first three words (e.g., 'Hyundai Santro Xing XO eRLX Euro III' became 'Hyundai Santro Xing').",object

📈 Cleaning Summary
The rigorous cleaning process significantly improved data quality, resulting in a robust dataset suitable for model training:
Metric,Original Data (892 Rows),Cleaned Data (Approx. 816 Rows)
Size Reduction,N/A,≈ 8% of rows dropped
Price Column,object (Mixed),int (Clean)
kms_driven,object (Mixed),int (Clean)
Missing Values,Present in 3 columns,Eliminated

The final cleaned dataset, is now ready for Feature Engineering and Model Training

