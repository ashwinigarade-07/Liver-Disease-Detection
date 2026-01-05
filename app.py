import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("liver_model.pkl", "rb"))

# Title
st.title("🩺 Liver Disease Prediction")
st.write("Enter patient details below to predict liver disease:")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, step=1)

gender = st.selectbox(
    "Gender",
    options=[0, 1],
    format_func=lambda x: "Female" if x == 0 else "Male"
)

total_bilirubin = st.number_input("Total Bilirubin", min_value=0.0, step=0.1)
direct_bilirubin = st.number_input("Direct Bilirubin", min_value=0.0, step=0.1)
alkaline_phosphotase = st.number_input("Alkaline Phosphotase", min_value=0.0, step=1.0)
alamine_aminotransferase = st.number_input("Alamine Aminotransferase", min_value=0.0, step=1.0)
aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase", min_value=0.0, step=1.0)
total_proteins = st.number_input("Total Proteins", min_value=0.0, step=0.1)
albumin = st.number_input("Albumin", min_value=0.0, step=0.1)
agr_ratio = st.number_input("Albumin and Globulin Ratio", min_value=0.0, step=0.1)

# Predict button
if st.button("Predict"):
    features = np.array([[age, gender, total_bilirubin, direct_bilirubin,
                          alkaline_phosphotase, alamine_aminotransferase,
                          aspartate_aminotransferase, total_proteins,
                          albumin, agr_ratio]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    st.subheader("🧪 Prediction Result:")
    if prediction == 1:
        st.error(f"⚠ Liver Disease Detected (probability: {probability:.2f})")
    else:
        st.success(f"✅ No Liver Disease Detected (probability: {probability:.2f})")
