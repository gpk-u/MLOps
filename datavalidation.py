import pandas as pd

df = pd.read_csv("inputspreadsheet.csv")
df["combined"] = df["subject"].fillna("")+" "+df["description"]

df["combined"].to_csv("inputs.txt", index=False)


