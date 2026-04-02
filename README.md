# Marketing Spend Optimization Engine

## Executive Summary

A marketing team is spending a fixed budget across 4 channels — TV, Digital, Influencer and Search — without knowing which allocation maximizes revenue. This project builds a decision analytics engine to answer that question, models diminishing returns across all channels, and delivers a concrete recommended allocation with predicted revenue outcome.

**Key Finding:** Digital delivers the highest marginal ROI across all budget scenarios. However, over-allocating to any single channel triggers diminishing returns — the optimal strategy is a diversified allocation weighted toward Digital and Search.

**Bottom Line:** Under a $530K budget, shift spend toward Digital (37%) and Search (27%), reduce Influencer to a supporting role, and expect a predicted revenue of $8,008.

---

## Business Questions Answered

* Which marketing channel delivers the highest return per dollar spent?
* How should a fixed budget be allocated across TV, Digital, Influencer and Search to maximize revenue?
* At what point does increasing spend on a channel stop paying off?
* What happens to predicted revenue under different budget cut or reallocation scenarios?

---

## Key Results

* **Digital is the highest ROI channel** across all 6 budget levels tested — it should anchor any allocation strategy
* **Diminishing returns are real and measurable** — doubling Digital spend does not double revenue, making diversification mathematically necessary
* **Optimal allocation under $530K budget:** TV 23%, Digital 37%, Search 27%, Influencer 13%
* **Predicted maximum revenue: $8,008** under the optimal allocation
* **7 scenarios simulated** — budget cuts, channel shifts and reallocations — giving the marketing team a decision playbook rather than a single answer

---

## Business Recommendations

* **Prioritize Digital in every budget scenario** — it consistently delivers the highest marginal return and should never be the first channel cut
* **Cap Influencer spend at 15%** — it shows the lowest ROI relative to cost and is the first candidate for reallocation
* **Do not over-index on any single channel** — diminishing returns make a diversified allocation mathematically superior to concentration
* **Use the scenario simulation as a decision tool** — when budget changes, run the model before reallocating rather than relying on intuition

---

## Methodology

1. Simulated realistic weekly marketing spend data across 4 channels
2. Built a multiple linear regression model with log-transformed features to capture diminishing returns
3. Validated model using R², VIF scores and residual diagnostics
4. Estimated marginal ROI per channel across 6 budget levels
5. Solved a constrained budget optimization problem using SciPy
6. Simulated 7 business scenarios including budget cuts, channel shifts and reallocations

---

## Tech Stack

* Python
* pandas, numpy
* statsmodels
* scipy

---

## How to Run
```bash
# 1. Create virtual environment and install requirements
pip install -r requirements.txt

# 2. Run in order
python src/model_setup.py
python src/regression_model.py
python src/simulation.py
python src/optimization.py
```

---

## What I Learned

Most marketing budget decisions are made on gut feel or last quarter's results. This project showed me how much value a simple regression and optimization layer can add — not by replacing judgment but by giving it a quantitative foundation. The most interesting insight was that the math actively discourages over-concentration, which is counterintuitive when one channel is clearly outperforming.
