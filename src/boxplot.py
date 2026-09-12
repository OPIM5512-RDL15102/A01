from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

figs = Path(__file__).resolve().parent.parent / "figs"
figs.mkdir(exist_ok=True)

df = fetch_california_housing(as_frame=True).frame

fig, axes = plt.subplots(1, 2, figsize=(9, 5))
axes[0].boxplot(df["MedInc"])
axes[0].set_title("Median Income")
axes[0].set_ylabel("Tens of thousands of USD")
axes[0].set_xticks([])
axes[0].grid(axis="y", alpha=0.3)
axes[1].boxplot(df["MedHouseVal"])
axes[1].set_title("Median House Value")
axes[1].set_ylabel("Hundreds of thousands of USD")
axes[1].set_xticks([])
axes[1].grid(axis="y", alpha=0.3)
fig.suptitle("California Housing (n = 20,640 block groups)")
fig.tight_layout()
fig.savefig(figs / "boxplot.png", dpi=150)
plt.close(fig)

fig, ax = plt.subplots(figsize=(9, 5))
ax.hist(df["HouseAge"], bins=range(1, 54), edgecolor="black")
ax.set_title("Distribution of Median House Age")
ax.set_xlabel("Years (capped at 52)")
ax.set_ylabel("Number of block groups")
ax.grid(axis="y", alpha=0.3)
fig.tight_layout()
fig.savefig(figs / "hist_houseage.png", dpi=150)
plt.close(fig)

print("Saved figs/boxplot.png and figs/hist_houseage.png")