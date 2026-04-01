import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB


# why index false ?
df = pd.read_csv("tickets.csv")
X_text = df["text"]
y = df["label"]
df.dropna(subset=["text", "label"])

vectorizer = TfidfVectorizer(ngram_range=(1,2))

X = vectorizer.fit_transform(X_text)
 # train model

model = LogisticRegression(max_iter=200, class_weight="balanced")
model.fit(X,y)


# save model

with open("model.pkl","wb") as f:
    pickle.dump((model,vectorizer),f)

print("Text model trained and saved")
