from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/predict")
async def predict():
    # Placeholder for model prediction logic
    return {"prediction": "result"}