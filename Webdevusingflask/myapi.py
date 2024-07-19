import paralleldots

class API:
  
  def __init__(self):
    paralleldots.set_api_key('IH4OCcC3pwUFU6jRcoyzug4ShpopFEtpLFigQEZImmk')
  
  def ner(self,text):
    response=paralleldots.ner(text)
    return response
  
  def sentiment_analysis(self,text):
        response=paralleldots.sentiment(text)
        return response
  
  def emotion_prediction(self,text):
        try:
            text_arr=[]
            text_arr.append(text)
            response=paralleldots.batch_emotion(text_arr)
            return response
        except Exception as e:
            return e
