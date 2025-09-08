# CFU Prediction Model (Random Forest)

This repository provides a **pre-trained random forest regression model** for predicting airborne microbial contamination (CFU) in operating rooms, based on indoor environmental parameters and particle concentrations.

---

## 🚀 Quick Start

1. **Clone this repository or download the files**  
   Make sure the following files are in the same directory:  
   - `rf_cfu_prediction_model.pkl` (the pre-trained model)  
   - `example_input.xlsx` (example input data)  
   - `example_prediction.py` (Python script to run predictions)

2. **Install required packages**

```bash
pip install pandas scikit-learn joblib openpyxl
```

3. **Run the example script**

```bash
python example_prediction.py
```

This will load the trained model, read the input data from `example_input.xlsx`, and print the predicted CFU concentration.

---

## 📥 Input Data Format

The model requires **10 features** as input. Make sure the column names in your Excel file match exactly:

| Feature      | Unit | Description                                |
|--------------|------|--------------------------------------------|
| temperature  | °C   | Indoor air temperature                     |
| RH           | %    | Relative humidity                          |
| CO2          | ppm  | Carbon dioxide concentration               |
| VOC          | ppb  | Volatile organic compounds                 |
| PM0.3        | #/L  | Particle count in 0.3–0.5 μm range         |
| PM0.5        | #/L  | Particle count in 0.5–1.0 μm range         |
| PM1          | #/L  | Particle count in 1.0–3.0 μm range         |
| PM3          | #/L  | Particle count in 3.0–5.0 μm range         |
| PM5          | #/L  | Particle count in 5.0–10.0 μm range        |
| PM10         | #/L  | Particle count in 10.0–25.0 μm range       |

See `example_input.xlsx` for a template.

---

## 🧪 Model Details

- Algorithm: Random Forest Regressor  
- Library: scikit-learn  
- Python version: 3.11.7  
- Training R² score: ~0.90  
- Trained on experimental data collected in a full-scale operating room under mixing ventilation

---

## 📧 Contact

For questions or scientific use, please contact:  
**Dr. Bi Yang**  
Shanghai Jiao Tong University  
📧 Email: yang.bi@sjtu.edu.cn  

---

**License**: This model is provided for academic and non-commercial research use only.
