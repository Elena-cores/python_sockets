import unittest
from Alerts import * 
from datetime import datetime

class Testalert(unittest.TestCase):
    def test_instancia_alert(self):
        alert = Alerts('DATE')
        self.assertEqual(alert.alert, 'DATE')
    
    def test_instancia_alert_2(self):
        alert = Alerts('TIME')
        self.assertEqual(alert.alert, 'TIME')

    def test_devolver_DATE(self):
        DATESys = datetime.now().date()
        alert = Alerts('DATE')
        DATEServ = alert.devolver_respuesta()
        self.assertEqual(DATESys, DATEServ)
    
    def test_devolver_TIME(self):
        TIMESys = datetime.now().strftime("%H:%M:%S")
        alert = Alerts('TIME')
        TIMEServ = alert.devolver_respuesta()
        self.assertEqual(TIMESys, TIMEServ)
    
    def test_devolver_error(self):
        alert = Alerts('Pongo una tontería')
        error = alert.devolver_respuesta()
        self.assertEqual('ERR', error)

if __name__=='__main__':
    unittest.main()