from setfit import SetFitModel
import logging


class SentimentAnalysisService:
    def __init__(self):
        self.model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")

    def sentiment_analysis(self, text):
        result = self.model([text])
        logging.info("Starting Sentiment result finding")
        # Extract the sentiment label
        sentiment = result[0].tolist()
        if sentiment == 1:
            prediction = 'Positive'
        elif sentiment == 0:
            prediction = 'Negative'
        else:
            prediction = 'Neutral'

        return prediction
