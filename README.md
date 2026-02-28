# Marketing Spend Optimization Engine

## Project Overview

This project builds a decision analytics engine to optimize multi-channel marketing budget allocation under a fixed total spend constraint.

The system models revenue as a function of:
- TV Spend
- Digital Spend
- Influencer Spend
- Search Spend

It incorporates diminishing returns using log transformations and solves a constrained optimization problem to determine the optimal allocation strategy.

---

## Methodology

1. Simulated realistic weekly marketing spend data.
2. Built Multiple Linear Regression model using log-transformed features.
3. Validated assumptions (R², VIF, residual diagnostics).
4. Estimated marginal ROI for each channel.
5. Implemented scenario simulation.
6. Solved constrained optimization problem using SciPy.

---

## Key Results

Under a fixed total budget of 530 units:

Optimal Allocation:
- TV: 121.80
- Digital: 197.97
- Influencer: 67.40
- Search: 142.83

Predicted Maximum Revenue: 8008.66

---

## Tech Stack

- Python
- pandas
- numpy
- statsmodels
- scipy

---

## Business Insight

The model demonstrates how diminishing returns prevent over-allocation to a single high-ROI channel and encourage diversified investment strategy.

---

## How to Run

1. Create virtual environment
2. Install requirements:

pip install -r requirements.txt

3. Run:
python src/model_setup.py
python src/regression_model.py
python src/simulation.py
python src/optimization.py
