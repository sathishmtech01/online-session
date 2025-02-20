import joblib
from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from scipy.stats import ks_2samp

# load model Deployment
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

app = FastAPI()

@app.post('/predict')
def predict(data: dict):
    try:
        review = [data['review']]
        transformed_review = vectorizer.transform(review)
        prediction = model.predict(transformed_review)
        sentiment = "Positive" if prediction[0] == 1 else "Negative"
        return {"prediction": sentiment}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
