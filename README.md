# Sales Performance & Customer Segmentation

This project leverages Python, SQL, and Power BI to perform comprehensive data analysis and machine learning for sales forecasting and customer segmentation.

## Project Overview
In today's retail landscape, shopping malls and Big Marts continuously track item-level sales data to anticipate customer demand and manage inventory effectively. By analyzing and mining this data from the data warehouse, the goal is to uncover anomalies and identify common patterns in customer behavior.

## Objective
The primary objective of this project is to build a solution that accurately predicts sales across different Big Mart stores. This model will allow stakeholders to make informed inventory decisions and optimize stock levels, improving overall efficiency.

## Project Workflow

### 1. Data Loading and Initial Exploration
- Loaded training and test datasets using Pandas.
- Performed basic data exploration using `head()`, `shape`, `info()`, and `describe()` to understand the structure and initial statistics of the data.

### 2. Exploratory Data Analysis (EDA)
- Checked for missing values in both training and test datasets.
- Used visualizations to understand the distribution of various categorical features and their counts and frequencies.
- Utilized the Sweetviz library to create an in-depth report of the dataset for further analysis.

### 3. Data Preprocessing
- **Missing Value Imputation:**
  - Filled missing values in `Item_Weight` with the mean of the column.
  - Imputed missing values in `Outlet_Size` using the mode as it is a categorical feature.
- **Feature Selection and Dropping Columns:**
  - Dropped `Item_Identifier` and `Outlet_Identifier` as they are not needed for model training.
- **Data Type Optimization:**
  - Converted object columns to categorical types to reduce memory usage.
  
### 4. Feature Engineering
- Created additional visualizations for understanding relationships between variables:
  - Created bar plots and line charts for categorical variables to show counts and frequencies.
  - Used box plots and scatter plots to analyze numerical variables and detect outliers.
- Generated an interactive box plot to explore numeric outliers in columns like `Item_Weight`, `Item_Visibility`, `Item_MRP`, and `Item_Outlet_Sales`.

### 5. Correlation Analysis
- Created a heatmap to analyze correlations between numerical variables and understand their relationships with each other, particularly with the target variable `Item_Outlet_Sales`.

### 6. Encoding Categorical Variables
- Encoded categorical variables using Label Encoding for model compatibility, particularly on the columns `Item_Fat_Content`, `Item_Type`, `Outlet_Size`, `Outlet_Location_Type`, and `Outlet_Type`.

### 7. Model Development
- **Model Selection:**
  - Trained and evaluated several models, including Linear Regression, Decision Tree, Random Forest, Gradient Boosting, XGBoost, CatBoost, and LightGBM.
  - Calculated Mean Absolute Error (MAE) for each model and compared them to select the best-performing model.
  
- **Hyperparameter Tuning:**
  - Performed Grid Search on Random Forest to identify the best combination of hyperparameters.
  
- **Final Model Selection:**
  - Chose Gradient Boosting as the final model based on its superior MAE score.
  - Retrained the Gradient Boosting model on the entire training set.

### 8. Model Evaluation and Visualization
- Evaluated the final model using metrics like R-squared, MAE, and RMSE.
- Visualized the performance of the final model with a scatter plot comparing actual and predicted values, and plotted a cumulative error distribution for a detailed error analysis.

### 9. Model Deployment
- Saved the final model using Joblib for deployment and created a Flask app to serve predictions through a web interface.
- Created a simple, responsive web app with an HTML form where users can input item features to receive sales predictions.
- Generated plots and visualizations dynamically in the web app, providing an interactive experience for users.

## Tools & Technologies
- **Programming Language:** Python
- **Database:** SQL
- **Data Visualization:** Power BI, Matplotlib, Seaborn, Plotly
- **Machine Learning Libraries:** Scikit-Learn, XGBoost, CatBoost, LightGBM
- **Deployment Framework:** Flask
- **Other Libraries:** Pandas, Sweetviz, Joblib, Webbrowser

## Results
This project provides actionable insights and accurate sales predictions, supporting data-driven decision-making for Big Mart’s inventory and customer management strategies. The model and insights allow Big Mart to optimize stock levels, improve sales forecasting, and identify key trends across different types of outlets.

## How to Run
1. Clone the repository and install the required libraries.
2. Run `app.py` using Python to start the Flask application.
3. Access the app via `http://127.0.0.1:9457` in your browser and enter the item details to get a sales prediction.
