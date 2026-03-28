import numpy as np
import pandas as pd

np.random.seed(42)

weeks = 120

tv_spend = np.random.normal(200, 40, weeks)
digital_spend = np.random.normal(150, 30, weeks)
influencer_spend = np.random.normal(80, 20, weeks)
search_spend = np.random.normal(100, 25, weeks)

# True impact coefficients (unknown in real life)
beta_tv = 3.5
beta_digital = 5.0
beta_influencer = 2.0
beta_search = 4.0

noise = np.random.normal(0, 200, weeks)

revenue = (
    beta_tv * np.log(tv_spend + 1) * 100 +
    beta_digital * np.log(digital_spend + 1) * 120 +
    beta_influencer * np.log(influencer_spend + 1) * 80 +
    beta_search * np.log(search_spend + 1) * 110 +
    noise
)

data = pd.DataFrame({
    "week": range(1, weeks + 1),
    "tv_spend": tv_spend,
    "digital_spend": digital_spend,
    "influencer_spend": influencer_spend,
    "search_spend": search_spend,
    "revenue": revenue
})
data.to_csv("data/marketing_data.csv", index=False)
print("Dataset created successfully.")
print(data.head())