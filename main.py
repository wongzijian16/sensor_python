# Do not run this example program directly. You run this program indirectly
# through the "launcher.py"

import time
from grovepi import *
from grove_rgb_lcd import *
import logging

log = logging.getLogger(__name__)

'''
D1: Light Bulb (Relay) and Buzzer
D3: Motion Sensor
A1: Thermistor (temperature sensor)
A2: Sound Sensor
D4: Car Reverse Sensor (ultrasonic)
D7: Water Level Sensor (ultrasonic)
D8: DHT (humidity and temperature sensor)
'''

state = 0             # Keep D1 state
#repeat = 100          # Repeat 100 times
sound_state = 0
setText('This uses fake modules for rapid development')
try:
#    while repeat > 0:
    while True:
        t, h = dht(8, 0)
        print(f'D1: {digitalRead(1)}, Motion Sensor: {digitalRead(3)},  ' 
              f'Sound: {analogRead(200)}, Car Ultrasonic: {ultrasonicRead(4)},  ')
        print(f'Thermistor: {temp(1):.2f}\xb0C,  DHT: {t}\xb0C, {h}%')
        state ^= 1
        digitalWrite(1, state)
        time.sleep(0.25)
except:
    log.exception('----------------Log----------------')

digitalWrite(1, 0)

