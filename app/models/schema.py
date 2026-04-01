from pydantic import BaseModel

class TicketInput(BaseModel):
    text: str