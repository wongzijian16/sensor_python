from time import *
import time
from grovepi import *
import datetime
from pyrebase import pyrebase


config = {
    "apiKey": "AIzaSyAGDakxqd8rK6x35nE3Mxp-hbZ2Kr6gOl8",
    "authDomain": "ff-management-database.firebaseapp.com",
    "databaseURL": "https://ff-management-database-default-rtdb.firebaseio.com",
    "storageBucket": "ff-management-database.appspot.com"

}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("jackiotassignment@.com", "jackiotassignment2022")
db = firebase.database()


temphumidhtsensor = 6
relay = 7
buzzer = 8

pinMode(temphumidhtsensor, "INPUT")
pinMode(relay, "OUTPUT")
pinMode(buzzer, "OUTPUT")

while True:

    try:

        sleep(2)

        [temperature, humidity] = dht(temphumidhtsensor, 0)

        hum = int(humidity)
        temp = int(temperature)
        currenttime = datetime.datetime.now()

        dhtresult = {"Humidity": hum, "Temperature": temp, "Datetime": str(currenttime)}

        dhtinformation = db.child("Frozen_Lorry").push(dhtresult, user['idToken'])

        # temp = 2-5 humi= 95-100
        if temperature <= 1 or temperature >= 6 or humidity <= 94 or humidity >= 101:
            relaylight = True
            buzzersound = True

        else:
            relaylight = False
            buzzersound = False

        if relaylight and buzzersound:
            digitalWrite(relay, 1)
            digitalWrite(buzzer, 1)
            time.sleep(1)
            digitalWrite(relay, 0)
            digitalWrite(buzzer, 0)
            digitalWrite(relay, 1)
            digitalWrite(buzzer, 1)
            time.sleep(1)
            digitalWrite(relay, 0)
            digitalWrite(buzzer, 0)

        else:
            print("good")

    except KeyboardInterrupt:
        print("Exited")
        break

    except TypeError:
        print("Type Error")

    except IOError:
        print("IO Error")
