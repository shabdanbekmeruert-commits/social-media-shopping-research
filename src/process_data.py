import pandas as pd
import numpy as np
import os

df = pd.read_csv("survey_sample.csv")

print("Missing values:", df.isnull().sum().sum())
print("Duplicates:", df.duplicated().sum())

columns = df.columns.drop("student_id")

Q1 = df[columns].quantile(0.25)
Q3 = df[columns].quantile(0.75)
IQR = Q3 - Q1

outliers = (
    (df[columns] < Q1 - 1.5 * IQR) |
    (df[columns] > Q3 + 1.5 * IQR)
)

print("Outliers:", outliers.sum().sum())

summary = pd.DataFrame({
    "Mean": df[columns].mean(),
    "SD": df[columns].std(),
    "Median": df[columns].median(),
    "p95": df[columns].quantile(0.95),
    "p99": df[columns].quantile(0.99)
})

np.random.seed(42)

ci_lower = []
ci_upper = []

for col in columns:
    data = df[col].dropna().values
    means = []

    for i in range(1000):
        sample = np.random.choice(
            data, size=len(data), replace=True
        )
        means.append(np.mean(sample))

    ci_lower.append(np.percentile(means, 2.5))
    ci_upper.append(np.percentile(means, 97.5))

summary["CI Lower"] = ci_lower
summary["CI Upper"] = ci_upper

os.makedirs("data/processed", exist_ok=True)

summary.to_csv(
    "data/processed/metrics_summary.csv",
    index_label="metric"
)

print("Processing completed successfully!")
