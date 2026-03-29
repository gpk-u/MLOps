import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# dataset
texts = [
    "free money now",
    "win cash prize",
    "hello how are you",
    "let's meet tomorrow",
    "urgent win reward",
    "are you coming today"
]

labels = [1, 1, 0, 0, 1, 0]  # 1 = spam, 0 = not spam

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
 # train model

model = MultinomialNB()
model.fit(X,labels)


# save model

with open("model.pkl","wb") as f:
    pickle.dump((model,vectorizer),f)

print("Text model trained and saved")
