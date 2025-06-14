# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 17:49:18 2025

@author: 91790
"""

import streamlit as st
import pickle
import pandas as pd

with open("rainfall_prediction_model.pkl", "rb") as file:
    model_data = pickle.load(file)

model = model_data["model"]
feature_names = model_data["feature_names"]

st.title("🌧️ Rainfall Prediction App")
st.write("Enter the weather conditions to predict whether it will rain.")

user_input = {}
for feature in feature_names:
    user_input[feature] = st.number_input(f"{feature.capitalize()}", format="%.2f")

input_df = pd.DataFrame([user_input])

if st.button("Predict"):
    prediction = model.predict(input_df)
    result = "🌧️ Rainfall expected" if prediction[0] == 1 else "☀️ No Rainfall"
    st.success(f"Prediction Result: {result}")
