import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# simulated ticket data
texts = [
    "cannot login to account",
    "password reset not working",
    "email not sending",
    "server is down",
    "application crash on startup",
    "need access to shared folder",
    "vpn not connecting",
    "system running very slow"
]

# labels (ticket categories)
labels = [
    "Access Issue",
    "Access Issue",
    "Email Issue",
    "Server Issue",
    "Application Issue",
    "Access Issue",
    "Network Issue",
    "Performance Issue"
]


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
 # train model

model = MultinomialNB()
model.fit(X,labels)


# save model

with open("model.pkl","wb") as f:
    pickle.dump((model,vectorizer),f)

print("Text model trained and saved")
