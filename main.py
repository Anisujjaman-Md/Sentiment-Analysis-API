from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from services.services import SentimentAnalysisService

app = FastAPI()
service = SentimentAnalysisService()


class SentimentRequest(BaseModel):
    text: str


@app.post('/analyze')
def analyze(request: SentimentRequest):
    text = request.text
    if not text:
        # Raise a 400 Bad Request if text is empty
        raise HTTPException(status_code=400, detail='Invalid request. Text is required.')
    prediction = service.sentiment_analysis(text)
    response = {'sentiment': prediction}
    return response
