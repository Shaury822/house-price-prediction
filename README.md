# 🏠 House Price Prediction System

A Machine Learning application that predicts residential property prices based on property features such as location, area, bedrooms, bathrooms, parking, property age, property type and furnishing.

## 📌 Project Objective

The objective of this project is to develop a machine learning regression model capable of predicting residential property prices.

## 🔧 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Random Forest Regression
- Streamlit
- Google Colab
- GitHub

## 📊 Features

The model uses the following features:

- Location
- Area (sqft)
- Bedrooms
- Bathrooms
- Parking
- Property Age
- Property Type
- Furnishing

## 🤖 Machine Learning Model

Random Forest Regression was used for house price prediction.

The preprocessing pipeline includes:

- Categorical feature encoding using OneHotEncoder
- Numerical feature processing
- Random Forest Regression

## 📈 Model Performance

| Metric | Score |
|---|---:|
| MAE | 15.77 |
| RMSE | 19.67 |
| R² Score | 0.9716 |

The model achieved an R² score of approximately 97.16%.

## 🏠 Prediction Interface

A Streamlit web application was developed where users can enter property details and receive a predicted house price.

## 📂 Project Structure

```text
house-price-prediction/
│
├── app.py
├── house_price_model.pkl
├── house_price_prediction.ipynb
├── README.md
├── requirements.txt
└── evaluation_report.md
