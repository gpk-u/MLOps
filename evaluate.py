import pandas as pd
from app.services.logic import predict_ticket

# load dataset
df = pd.read_csv("tickets.csv")

auto_correct = 0
auto_total = 0

suggest_correct = 0
suggest_total = 0

review_total = 0
rule_auto = 0
ml_auto = 0

for _, row in df.iterrows():
    pred = predict_ticket(row["text"])

    if pred["action"] == "auto":
        if pred["source"] == "rule":
            rule_auto += 1
        else:
            ml_auto += 1

print("Rule auto:", rule_auto)
print("ML auto:", ml_auto)

for _, row in df.iterrows():

    pred = predict_ticket(row["text"])

    if pred["action"] == "auto":
        auto_total += 1
        if pred["issue_bucket"] == row["label"]:
            auto_correct += 1

    elif pred["action"] == "suggest":
        suggest_total += 1
        if pred["issue_bucket"] == row["label"]:
            suggest_correct += 1

    else:
        review_total += 1


print("Auto accuracy:", auto_correct / auto_total if auto_total else 0)
print("Suggest accuracy:", suggest_correct / suggest_total if suggest_total else 0)
print("Review count:", review_total)