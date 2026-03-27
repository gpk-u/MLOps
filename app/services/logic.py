import pickle

with open("model.pkl","rb") as f:
    model = pickle.load(f)

def predict_price(area: int, rooms: int):
    prediction = model.predict([[area,rooms]])
    return int(prediction[0])

def cube(number: int):
    return number ** 3

def double(number: int):
    return number * 2