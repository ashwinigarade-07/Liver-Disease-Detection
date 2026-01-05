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

sex = st.selectbox(
    "Sex",
    options=[0, 1],
    format_func=lambda x: "Female" if x == 0 else "Male"
)

albumin = st.number_input("Albumin", min_value=0.0, step=0.1)

alkaline_phosphatase = st.number_input(
    "Alkaline Phosphatase", min_value=0.0, step=1.0
)

alanine_aminotransferase = st.number_input(
    "Alanine Aminotransferase (ALT)", min_value=0.0, step=1.0
)

aspartate_aminotransferase = st.number_input(
    "Aspartate Aminotransferase (AST)", min_value=0.0, step=1.0
)

bilirubin = st.number_input("Bilirubin", min_value=0.0, step=0.1)

cholinesterase = st.number_input("Cholinesterase", min_value=0.0, step=1.0)

cholesterol = st.number_input("Cholesterol", min_value=0.0, step=1.0)

creatinina = st.number_input("Creatinina", min_value=0.0, step=0.1)

gamma_glutamyl_transferase = st.number_input(
    "Gamma Glutamyl Transferase", min_value=0.0, step=1.0
)

protein = st.number_input("Protein", min_value=0.0, step=0.1)

# Predict button
if st.button("Predict"):
    features = np.array([[
        age,
        sex,
        albumin,
        alkaline_phosphatase,
        alanine_aminotransferase,
        aspartate_aminotransferase,
        bilirubin,
        cholinesterase,
        cholesterol,
        creatinina,
        gamma_glutamyl_transferase,
        protein
    ]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    st.subheader("🧪 Prediction Result:")
    if prediction == 1:
        st.error(f"⚠ Liver Disease Detected (probability: {probability:.2f})")
    else:
        st.success(f"✅ No Liver Disease Detected (probability: {probability:.2f})")
