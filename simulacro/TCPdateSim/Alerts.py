from datetime import datetime

class Alerts: 
    def __init__(self, alert):
        self.alert = alert

    def devolver_respuesta(self):
        if (self.alert=="DATE"):
            respuesta = datetime.now().date()
        elif (self.alert=="TIME"): 
            respuesta = datetime.now().strftime("%H:%M:%S")
        else:
            respuesta = 'ERR'
        return respuesta