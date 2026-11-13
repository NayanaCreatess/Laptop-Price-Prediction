import streamlit as st
import pandas as pd
import joblib

# Load saved model components
scaler = joblib.load('scaler.pkl')
pca = joblib.load('pca.pkl')
model = joblib.load('best_model.pkl')
feature_columns = joblib.load('feature_columns.pkl')

st.title("Laptop Price Category Prediction")
st.write("Enter laptop specifications to predict its price category.")

company = st.selectbox("Company", [
    "Acer", "Apple", "Asus", "Dell", "HP", "Lenovo",
    "MSI", "Toshiba", "Samsung", "Razer"
])

type_name = st.selectbox("Laptop Type", [
    "Notebook", "Ultrabook", "Gaming",
    "2 in 1 Convertible", "Workstation", "Netbook"
])

inches = st.number_input("Screen Size", 10.0, 20.0, 15.6)
screen_resolution = st.text_input("Screen Resolution", "1920x1080")
cpu = st.text_input("CPU", "Intel Core i5 7200U 2.5GHz")
ram = st.selectbox("RAM", ["4GB", "8GB", "16GB", "32GB"])
memory = st.text_input("Memory", "256GB SSD")
gpu = st.text_input("GPU", "Intel HD Graphics 620")
opsys = st.text_input("Operating System", "Windows 10")
weight = st.number_input("Weight (kg)", 0.5, 5.0, 2.0)

if st.button("Predict Price Category"):

    input_data = pd.DataFrame([{
        "Company": company,
        "TypeName": type_name,
        "Inches": inches,
        "ScreenResolution": screen_resolution,
        "Cpu": cpu,
        "Ram": float(ram.replace("GB", "")),
        "Memory": memory,
        "Gpu": gpu,
        "OpSys": opsys,
        "Weight": weight
    }])

    input_encoded = pd.get_dummies(input_data, dtype=int)

    input_encoded = input_encoded.reindex(
        columns=feature_columns,
        fill_value=0
    )

    input_scaled = scaler.transform(input_encoded)
    input_pca = pca.transform(input_scaled)

    prediction = model.predict(input_pca)[0]

    st.success(
        f"Predicted Laptop Price Category: {prediction}"
    )



