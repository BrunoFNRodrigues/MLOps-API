from fastapi import FastAPI

# loader functions that you programmed!
from model import load_model, load_encoder


app = FastAPI()


@app.get("/")
async def root():
    """
    Route to check that API is alive!
    """
    return "Model API is alive!"


@app.post("/predict")
async def predict():
    """
    Route to make predictions!
    """
    # Load the models
    ohe = load_encoder()
    model = load_model()

    return {"prediction": "I can almost make predictions!"}