import pandas as pd
import statsmodels.api as sm

# Load dataset
data = pd.read_csv("data/marketing_data.csv")

# Define features (X) and target (y)
import numpy as np

data["log_tv"] = np.log(data["tv_spend"] + 1)
data["log_digital"] = np.log(data["digital_spend"] + 1)
data["log_influencer"] = np.log(data["influencer_spend"] + 1)
data["log_search"] = np.log(data["search_spend"] + 1)

X = data[["log_tv", "log_digital", "log_influencer", "log_search"]]
y = data["revenue"]

# Add constant (intercept)
X = sm.add_constant(X)

# Build model
model = sm.OLS(y, X).fit()

# Print summary
print(model.summary())

from statsmodels.stats.outliers_influence import variance_inflation_factor

vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

print("\nVIF Scores:")
print(vif_data)

print("\nEstimated Marginal ROI per Channel:")
roi = model.params.drop("const")
print(roi)