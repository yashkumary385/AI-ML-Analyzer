from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load pipeline
pipeline = joblib.load("sentiment_analyzer_pipeline.pkl")

app = FastAPI()

# Pydantic model
class TextInput(BaseModel):
    text: str

# Simple home route
@app.get("/")
def home():
    return {"message": "API is working!"}

# Prediction route
@app.post("/predict")
def predict(input_data: TextInput):
    # Get prediction
    prediction = pipeline.predict([input_data.text])[0]

    # Ensure it's JSON-serializable
    if isinstance(prediction, (int, float, str)): # if any of these 
        if (prediction == 1):
           return {"sentiment Negative":  str(prediction)}
        else:
            return {"sentiment Positive":  str(prediction)}
    else:
          if (prediction == 1):
           return {"sentiment":  f" Negative {str(prediction)} "}
          elif(prediction ==2):
              return {"sentiment" : f"Neutral {str(prediction)}"}
          else:
            return {"sentiment": f" Positive {str(prediction)}"}
        # return {"sentiment": str(prediction)}
