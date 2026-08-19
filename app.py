
import streamlit as st
import pandas as pd
import joblib

import os
import joblib

model_path = os.path.join(os.path.dirname(__file__), "house_price_model.pkl")
model = joblib.load(model_path)

st.title("🏠 House Price Prediction")
st.write("Enter house details to predict the price.")

location = st.text_input("Location", "Mumbai")
area = st.number_input("Area (sqft)", min_value=100, value=1000)
bedrooms = st.number_input("Bedrooms", min_value=1, value=2)
bathrooms = st.number_input("Bathrooms", min_value=1, value=2)
parking = st.number_input("Parking", min_value=0, value=1)
age = st.number_input("Property Age (years)", min_value=0, value=5)
property_type = st.text_input("Property Type", "Apartment")
furnishing = st.text_input("Furnishing", "Semi-Furnished")

if st.button("Predict House Price"):

    new_house = pd.DataFrame({
        "Location": [location],
        "Area_sqft": [area],
        "Bedrooms": [bedrooms],
        "Bathrooms": [bathrooms],
        "Parking": [parking],
        "Property_Age_Years": [age],
        "Property_Type": [property_type],
        "Furnishing": [furnishing]
    })

    prediction = model.predict(new_house)

    st.success("Prediction completed!")

    st.metric(
        "Predicted House Price",
        f"{prediction[0]:.2f} Lakh"
    )

