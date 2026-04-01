from fastapi import APIRouter
from app.models.schema import TicketInput
from app.services.logic import predict_ticket


router = APIRouter()

@router.post("/predict-ticket")
def checktkt(data: TicketInput):
    result = predict_ticket(data.text)
    return{"issue_bucket": result}