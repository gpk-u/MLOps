from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Input schema
class InputData(BaseModel):
    number: int
@app.get("/")
def home():
    return {"message":"Hello"}
@app.post("/predict")
def predict(data: InputData):
    return {"result": data.number + 10}