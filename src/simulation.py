import numpy as np
import pandas as pd

# Load saved coefficients (from regression_model.py output)
coeffs = pd.read_csv("data/model_coefficients.csv", index_col=0, header=None, skiprows=1)
coeffs.columns = ["value"]
coeffs = coeffs["value"]

def predict_revenue(tv, digital, influencer, search):
    revenue = (
        coeffs["log_tv"] * np.log(tv + 1) +
        coeffs["log_digital"] * np.log(digital + 1) +
        coeffs["log_influencer"] * np.log(influencer + 1) +
        coeffs["log_search"] * np.log(search + 1) +
        coeffs["const"]
    )
    return revenue

# Baseline
baseline = (200, 150, 80, 100)
baseline_revenue = predict_revenue(*baseline)
print(f"Baseline Revenue: {baseline_revenue:.2f}")
print(f"Baseline Total Spend: {sum(baseline)}\n")

# Scenarios
scenarios = {
    "Baseline":                   (200, 150, 80, 100),
    "Increase Digital 20%":       (200, 180, 80, 100),
    "Reduce TV 20%":              (160, 150, 80, 100),
    "Shift TV Budget to Digital": (160, 190, 80, 100),
    "Cut Influencer, Boost Search":(200, 150, 40, 140),
    "20% Overall Budget Cut":     (160, 120, 64, 80),
    "20% Overall Budget Increase":(240, 180, 96, 120),
}

print("Scenario Comparisons:\n")
print(f"{'Scenario':<30} {'Revenue':>10} {'vs Baseline':>12} {'Total Spend':>12}")
print("-" * 68)

for name, values in scenarios.items():
    revenue = predict_revenue(*values)
    delta = revenue - baseline_revenue
    total_spend = sum(values)
    print(f"{name:<30} {revenue:>10.2f} {delta:>+12.2f} {total_spend:>12}")