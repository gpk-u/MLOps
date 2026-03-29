from fastapi import APIRouter
from app.models.schema import NumberInput, PredictInput, TextPredict
from app.services.logic import double, cube, predict_price, predict_spam

router = APIRouter()

@router.post("/predict")
def predict(data: PredictInput):
    result = predict_price(data.area,data.rooms)
    return {"price": result}

@router.post("/cube")
def cube_endpoint(data:NumberInput):
    result = cube(data.number)
    return {"result": result}

@router.post("/double")
def double_endpoint(data:NumberInput):
    result = double(data.number)
    return {"result": result}

@router.post("/predict-text")
def checktxt(data:TextPredict):
    result = predict_spam(data.text)
    return{"spam": result}