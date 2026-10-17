import streamlit as st
import pickle
import numpy as np

# Load model and columns
model = pickle.load(open("laptop_price_model.pkl", "rb"))
columns = pickle.load(open("model_columns.pkl", "rb"))

# Title
st.title("💻 Laptop Price Predictor")

# User Input
company = st.selectbox("Company", ["Apple", "HP", "Dell", "Lenovo", "Asus", "Acer", "MSI", "Toshiba", "Others"])
ram = st.slider("RAM (GB)", 4, 64, step=4)
gpu = st.selectbox("GPU Brand", ["Intel", "AMD", "Nvidia"])
opsys = st.selectbox("Operating System", ["Windows", "macOS", "Linux", "No OS"])
weight = st.number_input("Weight (kg)")
cpu_brand = st.selectbox("CPU Brand", ["Intel", "AMD", "Other"])
ssd = st.selectbox("SSD Size (GB)", [0, 128, 256, 512, 1000])
touchscreen = st.selectbox("Touchscreen", ["No", "Yes"])
ips = st.selectbox("IPS Display", ["No", "Yes"])
ppi = st.number_input("PPI (Pixels Per Inch)", min_value=50.0, max_value=400.0, value=120.0)

# Convert categorical to numerical (manual encoding, like you used in training)
def binary_map(feature):
    return 1 if feature == "Yes" else 0

company_dict = {"Apple": 0, "HP": 1, "Dell": 2, "Lenovo": 3, "Asus": 4, "Acer": 5, "MSI": 6, "Toshiba": 7, "Others": 8}
gpu_dict = {"Intel": 0, "AMD": 1, "Nvidia": 2}
opsys_dict = {"Windows": 0, "macOS": 1, "Linux": 2, "No OS": 3}
cpu_dict = {"Intel": 0, "AMD": 1, "Other": 2}

# Prepare data in correct order
input_data = np.array([
    company_dict[company],
    ram,
    gpu_dict[gpu],
    opsys_dict[opsys],
    weight,
    cpu_dict[cpu_brand],
    ssd,
    binary_map(touchscreen),
    binary_map(ips),
    ppi
]).reshape(1, -1)

# Predict
if st.button("Predict Price 💰"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Price:  €{int(prediction):,}")

