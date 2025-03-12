from FakeDevices import *
import logging

log = logging.getLogger(__name__)

# Modify only the code between try-except. Please leave the rest
# as it is.
try:
    gui = Gui()
    # Lines 13 - 24 are statements to initialize the fake devices
    # and add them into the GUI control panel.
    # You can add digital ports D0 to D9. Below, I use only D1 and D3.
    gui.add(DigitalPin(1, 'Light Bulb (Relay) and Buzzer', should_sound=True))
    gui.add(DigitalPin(3, 'Motion Sensor'))
    # You can add analog ports A0 to A2. Below I use only A1 and A2.
    gui.add(AnalogReadPin(1, 'Thermistor (\u2126)', min=1, max=1022))
    gui.add(AnalogReadPin(200, 'Sound Sensor (A2)'))
    # Ultrasonic is connected to D4. You can add more of this sensor
    # if you wish.
    gui.add(Ultrasonic(4, 'Car Reverse Sensor (mm)'))
    gui.add(Ultrasonic(7, 'Water Level (mm)'))
    # DHT -- temperature and humdity sensor is connected to D6.
    # You can have more than 1 DHT by adding more.
    gui.add(DHT(8, 'Room'))
    # Add your main Python program here. My example here is "main",
    # yours might be a different name. Please change accordingly.    
    from main import *
except:
    # Generate exception traceback to help debugging
    log.exception('----------------Log----------------')
    
# Make sure to call gui.quit(). Otherwise the GUI will not be closed
# after the program terminated.
gui.quit()
# Inform the user that the program has terminated
print('Program terminated.')
