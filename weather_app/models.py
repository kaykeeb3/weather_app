class Clima:
    def __init__(self, data):
        self.temperatura = data["main"]["temp"]
        self.descricao = data["weather"][0]["description"]
  
