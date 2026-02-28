import pandas as pd
import statsmodels.api as sm

# Load data
data = pd.read_csv("data/marketing_data.csv")

X = data[["tv_spend", "digital_spend", "influencer_spend", "search_spend"]]
y = data["revenue"]

X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

def predict_revenue(tv, digital, influencer, search):
    input_data = pd.DataFrame({
        "const": [1],
        "tv_spend": [tv],
        "digital_spend": [digital],
        "influencer_spend": [influencer],
        "search_spend": [search]
    })
    
    prediction = model.predict(input_data)
    return prediction.iloc[0]


# Example scenario
predicted = predict_revenue(250, 200, 70, 120)
print("Predicted Revenue:", predicted)

print("\nScenario Comparisons:\n")

scenarios = {
    "Baseline": (200, 150, 80, 100),
    "Increase Digital 20%": (200, 180, 80, 100),
    "Reduce TV 20%": (160, 150, 80, 100),
    "Shift TV to Digital": (170, 180, 80, 100)
}

for name, values in scenarios.items():
    revenue = predict_revenue(*values)
    print(f"{name}: {revenue:.2f}")