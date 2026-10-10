
import csv
import json
import math
import time
from pathlib import Path

# Project folders
ROOT = Path(__file__).resolve().parent.parent

# Read experiment settings
with open(ROOT / "configs/config.json", encoding="utf-8") as file:
    config = json.load(file)

input_path = ROOT / config["dataset"]["input_file"]
output_path = ROOT / config["dataset"]["output_file"]

start_time = time.perf_counter()

# Read sample survey data
with open(input_path, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Variables from our research
exposure = []
credibility = []
intention = []
decisions = []

valid_rows = 0
missing_rows = 0

required_columns = (
    ["student_id"]
    + config["variables"]["independent"]
    + config["variables"]["dependent"]
    + config["variables"]["controlled"]
)

if not data:
    raise ValueError("The sample dataset is empty.")

for column in required_columns:
    if column not in data[0]:
        raise ValueError(f"Missing column: {column}")

minimum = config["measurement"]["likert_min"]
maximum = config["measurement"]["likert_max"]
allowed_decisions = config["measurement"]["purchase_decision_values"]

for row in data:
    if any(not row[column].strip() for column in required_columns):
        missing_rows += 1
        continue

    try:
        scores = [
            int(row[column])
            for column in required_columns
            if column not in ("student_id", "purchase_decision")
        ]
        decision = int(row["purchase_decision"])

        if not all(minimum <= score <= maximum for score in scores):
            continue
        if decision not in allowed_decisions:
            continue

        exposure.append(int(row["advertising_exposure"]))
        credibility.append(int(row["perceived_credibility"]))
        intention.append(int(row["purchase_intention"]))
        decisions.append(decision)
        valid_rows += 1

    except ValueError:
        continue

if valid_rows < 3:
    raise ValueError("At least three valid responses are required.")


# Calculate average
def mean(values):
    return sum(values) / len(values)


# Average ranks, including tied values
def ranks(values):
    ordered = sorted(enumerate(values), key=lambda item: item[1])
    result = [0.0] * len(values)
    index = 0

    while index < len(ordered):
        end = index + 1
        while end < len(ordered) and ordered[end][1] == ordered[index][1]:
            end += 1

        average_rank = (index + 1 + end) / 2
        for position in range(index, end):
            result[ordered[position][0]] = average_rank

        index = end

    return result


# Spearman correlation
def spearman(x, y):
    rx = ranks(x)
    ry = ranks(y)

    mx = mean(rx)
    my = mean(ry)

    numerator = sum(
        (a - mx) * (b - my)
        for a, b in zip(rx, ry)
    )

    denominator = math.sqrt(
        sum((a - mx) ** 2 for a in rx)
        * sum((b - my) ** 2 for b in ry)
    )

    if denominator == 0:
        return None

    return numerator / denominator


total_rows = len(data)

# Main research measurements
exposure_correlation = spearman(exposure, intention)
credibility_correlation = spearman(credibility, intention)

# Data quality checks
missing_value_rate = missing_rows / total_rows
valid_response_rate = valid_rows / total_rows
purchase_decision_rate = mean(decisions)

execution_time = time.perf_counter() - start_time

results = {
    "project": config["project_name"],
    "sample_type": config["dataset"]["sample_type"],
    "total_responses": total_rows,
    "valid_responses": valid_rows,
    "primary_metric": {
        "name": "spearman_correlation",
        "advertising_exposure_vs_purchase_intention": exposure_correlation
    },
    "secondary_metrics": {
        "credibility_vs_purchase_intention": credibility_correlation,
        "mean_purchase_intention": mean(intention),
        "purchase_decision_rate": purchase_decision_rate
    },
    "guardrail_metrics": {
        "missing_value_rate": missing_value_rate,
        "valid_response_rate": valid_response_rate
    },
    "baseline_correlation": config["benchmark"]["baseline_correlation"],
    "execution_time_seconds": execution_time
}

# Save results
output_path.parent.mkdir(parents=True, exist_ok=True)

with open(output_path, "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4)

print(json.dumps(results, indent=4))
print(f"\nResults saved to: {output_path}")
