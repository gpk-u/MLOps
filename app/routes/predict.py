from fastapi import APIRouter
from app.models.schema import NumberInput, PredictInput, TextPredict, TicketInput
from app.services.logic import double, cube, predict_price, predict_spam, predict_ticket

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

@router.post("/predict-ticket")
def checktkt(data: TicketInput):
    result = predict_ticket(data.text)
    return{"category": result}