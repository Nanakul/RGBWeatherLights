import time
import RPi.GPIO as GPIO

#Relay Code
'''
IN on the relay goes to pin 15, DC- on the relay goes to ground, DC+ goes to 5V
'''

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
RELAIS_1_GPIO = 15 #GPIO Pin 15 (Which is pin 10 on the pinout chart)
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
st = time.time() #when we start counting the time

try:

    while time.time() - st < 30: #start time (current time) - time you started while < 30 seconds.. after 30 seconds, stop.
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # off
        time.sleep(4)
        GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on
        time.sleep(4)

except:
    GPIO.cleanup()