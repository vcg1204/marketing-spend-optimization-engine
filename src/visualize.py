import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Create outputs folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Load data
data = pd.read_csv("data/marketing_data.csv")
coeffs = pd.read_csv("data/model_coefficients.csv", index_col=0, header=None, skiprows=1)
coeffs.columns = ["value"]
coeffs = coeffs["value"]
optimization_results = pd.read_csv("data/optimization_results.csv")

# ── Chart 1: Spend vs Revenue curves per channel ──────────────────────────────
spend_range = np.linspace(10, 400, 200)

channels = {
    "TV":         ("log_tv",         "steelblue"),
    "Digital":    ("log_digital",    "darkorange"),
    "Influencer": ("log_influencer", "green"),
    "Search":     ("log_search",     "crimson"),
}

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for i, (channel, (coeff_key, color)) in enumerate(channels.items()):
    revenue = coeffs[coeff_key] * np.log(spend_range + 1)
    axes[i].plot(spend_range, revenue, color=color, linewidth=2)
    axes[i].set_title(f"{channel} — Diminishing Returns Curve", fontsize=11)
    axes[i].set_xlabel("Spend")
    axes[i].set_ylabel("Revenue Contribution")
    axes[i].grid(True, alpha=0.3)

plt.suptitle("Marketing Channel Diminishing Returns", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/diminishing_returns_curves.png", dpi=150)
plt.close()
print("Saved: diminishing_returns_curves.png")

# ── Chart 2: Optimal allocation bar chart at budget = 530 ─────────────────────
row_530 = optimization_results[optimization_results["budget"] == 530].iloc[0]

channels_list = ["TV", "Digital", "Influencer", "Search"]
allocations = [row_530["tv"], row_530["digital"], row_530["influencer"], row_530["search"]]
colors = ["steelblue", "darkorange", "green", "crimson"]

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(channels_list, allocations, color=colors, edgecolor="white", width=0.5)

for bar, val in zip(bars, allocations):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2,
            f"{val:.1f}", ha="center", va="bottom", fontsize=10)

ax.set_title("Optimal Budget Allocation at Total Spend = 530", fontsize=13, fontweight="bold")
ax.set_ylabel("Spend Allocated")
ax.set_ylim(0, max(allocations) * 1.15)
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("outputs/optimal_allocation_530.png", dpi=150)
plt.close()
print("Saved: optimal_allocation_530.png")

# ── Chart 3: Revenue vs Budget (optimization across budgets) ──────────────────
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(optimization_results["budget"], optimization_results["revenue"],
        marker="o", color="steelblue", linewidth=2, markersize=6)

for _, row in optimization_results.iterrows():
    ax.annotate(f"{row['revenue']:.0f}",
                (row["budget"], row["revenue"]),
                textcoords="offset points", xytext=(0, 8), ha="center", fontsize=8)

ax.set_title("Predicted Revenue vs Total Marketing Budget", fontsize=13, fontweight="bold")
ax.set_xlabel("Total Budget")
ax.set_ylabel("Predicted Revenue")
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("outputs/revenue_vs_budget.png", dpi=150)
plt.close()
print("Saved: revenue_vs_budget.png")

# ── Chart 4: Channel allocation shift across budgets ──────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(optimization_results["budget"], optimization_results["tv"],
        marker="o", label="TV", color="steelblue", linewidth=2)
ax.plot(optimization_results["budget"], optimization_results["digital"],
        marker="o", label="Digital", color="darkorange", linewidth=2)
ax.plot(optimization_results["budget"], optimization_results["influencer"],
        marker="o", label="Influencer", color="green", linewidth=2)
ax.plot(optimization_results["budget"], optimization_results["search"],
        marker="o", label="Search", color="crimson", linewidth=2)

ax.set_title("How Optimal Channel Allocation Shifts with Budget", fontsize=13, fontweight="bold")
ax.set_xlabel("Total Budget")
ax.set_ylabel("Spend Allocated to Channel")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("outputs/allocation_shift_by_budget.png", dpi=150)
plt.close()
print("Saved: allocation_shift_by_budget.png")

print("\nAll charts saved to /outputs folder.")