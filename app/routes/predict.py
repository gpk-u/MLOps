from fastapi import APIRouter
from app.models.schema import InputData
from app.services.logic import calculate, double, cube, predict_price

router = APIRouter()

@router.post("/predict")
def predict(data: InputData):
    result = predict_price(data.number)
    return {"result": result}

@router.post("/cube")
def cube_endpoint(data:InputData):
    result = cube(data.number)
    return {"result": result}

@router.post("/double")
def double_endpoint(data:InputData):
    result = double(data.number)
    return {"result": result}