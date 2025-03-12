from FakeDevices import *
import logging

log = logging.getLogger(__name__)

try:
    gui = Gui()

    gui.add(DHT(6, 'Frozen Lorry', initial_humidity=98, initial_temp=3))
    gui.add(DigitalPin(7, 'Relay'))
    gui.add(DigitalPin(8, 'Buzzer', should_sound=True))

    from deliveryDHTsensor import *

except:

    log.exception('----------------Log----------------')


gui.quit()

print('Program terminated.')