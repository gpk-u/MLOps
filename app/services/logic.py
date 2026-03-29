import pickle
from train import vectorizer as vc


with open("model.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)

def predict_price(area: int, rooms: int):
    prediction = model.predict([[area,rooms]])
    return int(prediction[0])

def cube(number: int):
    return number ** 3

def double(number: int):
    return number * 2

def predict_spam(text: str):
    X = vectorizer.transform([text])
    prediction = model.predict(X)
    return int(prediction[0])

def predict_ticket(text: str):
    X=vectorizer.transform([text])
    prediction = model.predict(X)
    return prediction[0]