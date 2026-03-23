from fastapi import APIRouter
from app.models.schema import InputData
from app.services.logic import calculate

router = APIRouter()

@router.post("/predict")
def predict(data: InputData):
    result = calculate(data.number)
    return {"result": result}