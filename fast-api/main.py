from fastapi import FastAPI
from pydantic import BaseModel
from model import Model


app = FastAPI()
clf = Model()


class Item(BaseModel):
    Pclass: int
    Age: int
    Sex: str


@app.post("/predict")
async def predict(item: Item):
    return clf.predict([item.dict()])
