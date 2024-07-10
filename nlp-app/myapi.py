import paralleldots

class API:
    
    def __init__(self):
        paralleldots.set_api_key('IH4OCcC3pwUFU6jRcoyzug4ShpopFEtpLFigQEZImmk')
    
    def sentiment_analysis(self,text):
        response=paralleldots.sentiment(text)
        return response
    
    def ner(self,text):
        response=paralleldots.ner(text)
        return response
    
    def emotion_prediction(self,text):
        try:
            response=paralleldots.emotion(text)
            return response
        except Exception as e:
            return e
    