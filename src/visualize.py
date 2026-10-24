import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("survey_sample.csv")

sns.set_theme(
    style="whitegrid",
    palette="colorblind",
    font_scale=1.2
)

os.makedirs("reports/figures", exist_ok=True)

fig, ax = plt.subplots(figsize=(9, 6))

sns.regplot(
    data=df,
    x="advertising_exposure",
    y="purchase_intention",
    ci=95,
    color="tab:blue",
    scatter_kws={"s": 70, "alpha": 0.8},
    line_kws={"linestyle": "--"},
    ax=ax
)

ax.set_xlabel("Advertising Exposure (score)")
ax.set_ylabel("Purchase Intention (score)")
ax.set_title("Advertising Exposure vs Purchase Intention")
ax.set_xticks([1, 2, 3, 4, 5])
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_xlim(0.5, 5.5)
ax.set_ylim(0.5, 5.5)

fig.tight_layout()
fig.savefig("reports/figures/advertising_vs_intention.pdf")
fig.savefig("reports/figures/advertising_vs_intention.png", dpi=300)
plt.close(fig)

fig, ax = plt.subplots(figsize=(9, 6))

sns.boxplot(
    data=df[["advertising_exposure", "purchase_intention"]],
    palette="colorblind",
    ax=ax
)

ax.set_xlabel("Research Variables")
ax.set_ylabel("Score (1-5)")
ax.set_title("Distribution of Survey Responses")
ax.set_ylim(0, 6)

fig.tight_layout()
fig.savefig("reports/figures/distribution.pdf")
fig.savefig("reports/figures/distribution.png", dpi=300)
plt.close(fig)

print("Visualization completed successfully!")
