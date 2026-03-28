import numpy as np
import pandas as pd
from scipy.optimize import minimize

# Load saved coefficients (from regression_model.py output)
coeffs = pd.read_csv("data/model_coefficients.csv", index_col=0, header=None, skiprows=1)
coeffs.columns = ["value"]
coeffs = coeffs["value"]

def predict_revenue(spend):
    tv, digital, influencer, search = spend
    return (
        coeffs["log_tv"] * np.log(tv + 1) +
        coeffs["log_digital"] * np.log(digital + 1) +
        coeffs["log_influencer"] * np.log(influencer + 1) +
        coeffs["log_search"] * np.log(search + 1) +
        coeffs["const"]
    )

def objective(spend):
    return -predict_revenue(spend)

def budget_constraint(spend, budget):
    return sum(spend) - budget

bounds = [(10, None), (10, None), (10, None), (10, None)]
initial_guess = [200, 150, 80, 100]

# Run optimization across multiple budget levels
budgets = [400, 450, 500, 530, 600, 700]

print(f"{'Budget':<10} {'TV':>8} {'Digital':>10} {'Influencer':>12} {'Search':>10} {'Revenue':>10}")
print("-" * 65)

results = []

for budget in budgets:
    constraints = {"type": "eq", "fun": lambda s, b=budget: budget_constraint(s, b)}
    result = minimize(objective, initial_guess, bounds=bounds, constraints=constraints, method="SLSQP")
    
    if result.success:
        tv, digital, influencer, search = result.x
        revenue = -result.fun
        results.append({
            "budget": budget,
            "tv": tv,
            "digital": digital,
            "influencer": influencer,
            "search": search,
            "revenue": revenue
        })
        print(f"{budget:<10} {tv:>8.2f} {digital:>10.2f} {influencer:>12.2f} {search:>10.2f} {revenue:>10.2f}")

# Save results
results_df = pd.DataFrame(results)
results_df.to_csv("data/optimization_results.csv", index=False)
print("\nOptimization results saved to data/optimization_results.csv")