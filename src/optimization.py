import pandas as pd
import statsmodels.api as sm
from scipy.optimize import minimize

# Load data
data = pd.read_csv("data/marketing_data.csv")

import numpy as np

data["log_tv"] = np.log(data["tv_spend"] + 1)
data["log_digital"] = np.log(data["digital_spend"] + 1)
data["log_influencer"] = np.log(data["influencer_spend"] + 1)
data["log_search"] = np.log(data["search_spend"] + 1)

X = data[["log_tv", "log_digital", "log_influencer", "log_search"]]
y = data["revenue"]

X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

coeffs = model.params

# Objective function (negative because we minimize)
import numpy as np

def objective(spend):
    tv, digital, influencer, search = spend
    
    revenue = (
        coeffs["log_tv"] * np.log(tv + 1) +
        coeffs["log_digital"] * np.log(digital + 1) +
        coeffs["log_influencer"] * np.log(influencer + 1) +
        coeffs["log_search"] * np.log(search + 1)
    )
    
    return -revenue

# Constraint: total budget = 530
def budget_constraint(spend):
    return sum(spend) - 530

constraints = ({
    'type': 'eq',
    'fun': budget_constraint
})

bounds = [(0, None), (0, None), (0, None), (0, None)]

initial_guess = [200, 150, 80, 100]

result = minimize(objective, initial_guess, bounds=bounds, constraints=constraints)

optimal_spend = result.x

print("Optimal Allocation:")
print(f"TV: {optimal_spend[0]:.2f}")
print(f"Digital: {optimal_spend[1]:.2f}")
print(f"Influencer: {optimal_spend[2]:.2f}")
print(f"Search: {optimal_spend[3]:.2f}")

print("\nMaximum Predicted Revenue:")
print(-result.fun)