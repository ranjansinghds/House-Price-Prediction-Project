# 🏠 California House Price Prediction

A Machine Learning project that predicts the **median house value in California** based on different housing features.

The project covers the complete Machine Learning workflow, including:

- Data loading
- Exploratory Data Analysis (EDA)
- Data preprocessing
- Train-test split
- Model comparison
- Cross-validation
- Hyperparameter tuning
- Model evaluation
- Residual analysis
- Model saving
- Prediction on new data
- Streamlit web interface

---

## 📌 Project Overview

The goal of this project is to build a Machine Learning regression model that predicts:

> **Median House Value (`median_house_value`)**

using information such as:

1. longitude: A measure of how far west a house is; a higher value is farther west<br>
2. latitude: A measure of how far north a house is; a higher value is farther north<br>
3. housingMedianAge: Median age of a house within a block; a lower number is a newer building<br>
4. totalRooms: Total number of rooms within a block<br>
5. totalBedrooms: Total number of bedrooms within a block<br>
6. population: Total number of people residing within a block<br>
7. households: Total number of households, a group of people residing within a home unit, for a block<br>
8. medianIncome: Median income for households within a block of houses (measured in tens of thousands of US Dollars)<br>
9. medianHouseValue: Median house value for households within a block (measured in US Dollars)<br>
10. oceanProximity: Location of the house w.r.t ocean/sea

The **California Housing dataset** is used for this project.

---

## 🚀 Installation

### 1️⃣ Clone the repository:

```bash
git clone https://github.com/ranjansinghds/house-price-prediction-ml-project.git
cd HOUSE_PRICE_PREDICTION

### 2️⃣ Install dependencies:

Ensure you have the following Python packages installed:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

You can install them using pip:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## 🔍 Methodology

### 1. Exploratory Data Analysis

Several EDA techniques are performed to understand the dataset.

- **Missing Values**: Used to identify missing values in each column.
- **Duplicate Values**: Used to identify duplicate rows.
- **Feature Distributions**: Histograms are used to understand the distribution of numerical features.
- **Outlier Analysis**: Boxplots are used to identify potential outliers.
- **Correlation Analysis**: A correlation heatmap is used to understand relationships between numerical features.

### 2. Data Preprocessing

- **Numerical Features**: The following steps are applied:
Missing Values -> Median Imputation -> StandardScaler
- **Categorical Features**: The following steps are applied:
Missing Values -> Most Frequent Imputation -> One-Hot Encoding
- **ColumnTransformer**: is used to apply the appropriate preprocessing to numerical and categorical columns.

### 3. Predictive Modeling

- **Price Prediction**: Developed Hist Gradient Boosting Regressor models to predict House Price Prediction.
- **Model Evaluation**: Assessed model performance using metrics such as Mean Absolute Error (MAE), Root Mean Squared Error (RSE) and R2.

## 📊 Visualizations
Here are some visualizations from the project:

![alt text](https://github.com/ranjansinghds/house-price-prediction-ml-project/blob/main/House%20Price%20Prediction%20Project%20Png/Distribution%20of%20Ocean%20proximity.png)
![alt text](https://github.com/ranjansinghds/house-price-prediction-ml-project/blob/main/House%20Price%20Prediction%20Project%20Png/Target%20column%20distribution.png)
![alt text](https://github.com/ranjansinghds/house-price-prediction-ml-project/blob/main/House%20Price%20Prediction%20Project%20Png/correlation%20heatmap.png)
![alt text](https://github.com/ranjansinghds/house-price-prediction-ml-project/blob/main/House%20Price%20Prediction%20Project%20Png/histogram%20plot%20-%20distribution.png)
![alt text](https://github.com/ranjansinghds/house-price-prediction-ml-project/blob/main/House%20Price%20Prediction%20Project%20Png/outliers%20analysis%20-%20boxplot.png)

## 🛠️ Technologies Used

- Python
- Pandas & NumPy
- Matplotlib & Seaborn
- Scikit-learn
- Jupyter Notebook

## 📌 Future Improvements

- Add more advanced models
- Improve UI design
- Add prediction history
- Add interactive visualizations
- Deploy the Streamlit application online
- Add model performance charts
- Add automated data validation

