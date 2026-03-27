from pydantic import BaseModel

class PredictInput(BaseModel):
    rooms: int
    area: int

class NumberInput(BaseModel):
    number: int
    