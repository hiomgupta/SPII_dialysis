import streamlit as st
import joblib
import numpy as np

# Load model and feature order
model = joblib.load("dialysis_rf_model.pkl")
features = joblib.load("feature_order.pkl")

st.title("🩸 Blood Dialysis Concentration Predictor")
st.markdown("Predict the outlet solute concentration from hollow fiber dialysis model.")

# Sidebar sliders
user_input = []
st.sidebar.header("🛠 Input Parameters")

ranges = {
    "Rhf (mm)": (0.1, 1.5),
    "Lm (mm)": (0.05, 1.0),
    "Lpc (mm)": (0.2, 2.0),
    "H (mm)": (21, 21),  # Fixed if needed
    "K": (0.5, 3.0),
    "Uave_dia (mm/s)": (0.1, 2.0),
    "Uave_per (mm/s)": (0.1, 2.0),
    "c0_dia (mol/m^3)": (100, 2000),
    "c0_mem (mol/m3)": (0, 1000)
}

for f in features:
    min_val, max_val = ranges[f]
    val = st.sidebar.slider(f, min_value=float(min_val), max_value=float(max_val), value=float((min_val + max_val)/2))
    user_input.append(val)

# Prediction
input_array = np.array(user_input).reshape(1, -1)
pred = model.predict(input_array)[0]
st.success(f"🔬 Predicted Outlet Concentration: **{pred:.2f} mol/m³**")
    