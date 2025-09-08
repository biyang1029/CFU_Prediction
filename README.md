# CFU Prediction Model (Random Forest)

This repository provides a pre-trained random forest regression model for predicting airborne microbial contamination (CFU) in operating rooms, based on real-time environmental parameters.

## 🧪 Model Details

- Algorithm: Random Forest Regressor
- Library: scikit-learn
- Python Version: 3.11.7
- Training R² score: 0.90
- Trained on experimental data collected in a full-scale operating room under mixed ventilation

## 📂 Files Included

- `rf_cfu_prediction_model.pkl` — Pre-trained random forest model (binary format, for Python use)
- `example_input.xlsx` — Example input file with correct column names and data format
- '
## 📥 How to Use the Model

### 1. Install required packages
2. Load model and predict CFU
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("rf_cfu_prediction_model.pkl")

# Load your input data (make sure column names match)
input_df = pd.read_excel("example_input.xlsx")

# Predict CFU
cfu_prediction = model.predict(input_df)
print("Predicted CFU:", cfu_prediction)

Input Features Required
Feature	Unit	Description
temperature	°C	Indoor air temperature
RH	%	Relative humidity
CO2	ppm	Carbon dioxide concentration
VOC	ppb	Volatile organic compounds
PM0.3	#/L	Particle count in 0.3–0.5 μm range
PM0.5	#/L	Particle count in 0.5–1.0 μm range
PM1	#/L	Particle count in 1.0–3.0 μm range
PM3	#/L	Particle count in 3.0–5.0 μm range
PM5	#/L	Particle count in 5.0–10.0 μm range
PM10	#/L	Particle count in 10.0–25.0 μm range

For questions or scientific use, please contact:
Dr. Bi Yang
Shanghai Jiao Tong University
yang.bi@sjtu.edu.cn
