from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class DataModel(BaseModel):
    data: str

@app.post("/api/send_data")
async def send_data(data: DataModel):
    print(data)
    return {"message": "Данные получены"}