
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("rf_cfu_prediction_model.pkl")

# Load your input data (make sure column names match exactly)
input_df = pd.read_excel("example_input.xlsx")

# Predict CFU
cfu_prediction = model.predict(input_df)
print("Predicted CFU:", cfu_prediction)
