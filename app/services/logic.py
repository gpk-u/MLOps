import pickle

with open("model.pkl","rb") as f:
    model = pickle.load(f)

def predict_price(area: int):
    prediction = model.predict([[area]])
    return int(prediction[0])


def calculate(number: int):
    return number * 10

def cube(number: int):
    return number ** 3

def double(number: int):
    return number * 2