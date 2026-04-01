import pandas as pd

#load
df = pd.read_csv("tpms400.csv")

# combine text
df["text"] = df["Subject"].fillna("")+" "+df["Description"].fillna("")

#label
df["label"] = df["Issue Buckets"].fillna("")

#clean
df = df.dropna(subset=["text","label"])
df = df[df["label"].astype(str).str.strip() != ""]
df = df[df["text"].astype(str).str.strip() != ""]


df ["label"] = df["label"].astype(str).str.strip()


#check distribution
print("\nLabel Distribution BEFORE:")
print(df["label"].value_counts())

#balance all classes

target_size = 50

df_balanced = df.groupby("label").apply(
    lambda x: x.sample(min(len(x), target_size), random_state=42)
).reset_index(drop=True)

#final dataset

df_final = df_balanced[["text", "label"]]

df_final.to_csv("tickets.csv", index=False)

print("\nLabel Distribution AFTER:")
print(df_final["label"].value_counts())

print("\nDataset ready")