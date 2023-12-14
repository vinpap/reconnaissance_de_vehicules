import torch
from fastapi import FastAPI

from model import predict


# Initializes the (small) network from ultralytics
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')


app = FastAPI()

@app.get("/")
async def root(img_path: str) -> float:
    prediction = predict(model, img_path)
    return prediction
