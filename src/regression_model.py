import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Load data
data = pd.read_csv("data/marketing_data.csv")

# Log transform features (diminishing returns)
data["log_tv"] = np.log(data["tv_spend"] + 1)
data["log_digital"] = np.log(data["digital_spend"] + 1)
data["log_influencer"] = np.log(data["influencer_spend"] + 1)
data["log_search"] = np.log(data["search_spend"] + 1)

X = data[["log_tv", "log_digital", "log_influencer", "log_search"]]
y = data["revenue"]
X = sm.add_constant(X)

# Fit OLS model
model = sm.OLS(y, X).fit()
print(model.summary())

# VIF check
vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print("\nVIF Scores:")
print(vif_data)

# Marginal ROI per channel
print("\nEstimated Marginal ROI per Channel:")
print(model.params.drop("const"))

# Save coefficients for use in other scripts
model.params.to_csv("data/model_coefficients.csv")
print("\nCoefficients saved to data/model_coefficients.csv")