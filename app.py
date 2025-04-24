import streamlit as st
import joblib
import numpy as np

# Load model and features
model = joblib.load("dialysis_rf_model.pkl")
features = joblib.load("feature_order.pkl")

# Define parameter ranges (can update based on your actual dataset)
ranges = {
    "Rhf (mm)": (0.1, 1.5),
    "Lm (mm)": (0.05, 1.0),
    "Lpc (mm)": (0.2, 2.0),
    "H (mm)": (21, 21),  # Fixed, so use number_input
    "K": (0.5, 3.0),
    "Uave_dia (mm/s)": (0.1, 2.0),
    "Uave_per (mm/s)": (0.1, 2.0),
    "c0_dia (mol/m^3)": (100, 2000),
    "c0_mem (mol/m3)": (0, 1000)
}

# App UI
st.set_page_config(page_title="Dialysis Outlet Concentration Predictor", layout="centered")
st.title("🩸 Dialysis Simulation: Solute Concentration Predictor")
st.markdown("This app predicts the **outlet solute concentration** based on parameters of a hollow-fiber dialysis membrane. Adjust the parameters on the left and get real-time predictions!")

st.sidebar.header("🛠 Set Input Parameters")
user_input = []

# Build sidebar sliders / number inputs
for f in features:
    min_val, max_val = ranges[f]
    if min_val == max_val:
        val = st.sidebar.number_input(f, value=float(min_val), step=0.1)
    else:
        val = st.sidebar.slider(
            f,
            min_value=float(min_val),
            max_value=float(max_val),
            value=float((min_val + max_val) / 2),
            step=(max_val - min_val) / 100
        )
    user_input.append(val)

# Prediction
input_array = np.array(user_input).reshape(1, -1)
pred = model.predict(input_array)[0]

# Output
st.subheader("🔍 Predicted Outlet Solute Concentration")
st.success(f"💧 {pred:.2f} mol/m³")

# Footer
st.markdown("---")
st.caption("Developed using COMSOL & Streamlit • IIT Gandhinagar Project")
