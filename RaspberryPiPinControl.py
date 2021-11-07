import time
import RPi.GPIO as GPIO
import matplotlib.colors as colors

def setrgbGPIO(pins = [17, 27, 22], pwmFreq = 50):
    setPins = [] 

#Set GPIO pins
    GPIO.setmode(GPIO.BCM)

    for pin in pins: #initializing the pins
        GPIO.setup(pin, GPIO.OUT) #set pins up to output
        setPins.append(GPIO.PWM(pin, pwmFreq)) # adding an object that represents a pin in PWM mode; setting up so I can output a range of values.
        setPins[-1].start(0) #starting the pin
    
    return setPins

def convertColor(x): # Takes a color between 0 and 255 and converts it to the same thing, but on a scale of 0 to 100.
   y = (100 * (x / 255))
   return int(y)

def setColor(CurrentPins, r = 0,g = 0,b = 0): # This function takes 3 values (r,g,b set to 0)
    trueR = convertColor(r)
    trueG = convertColor(g)
    trueB = convertColor(b)

    print(f'Setting pins to: {trueR}, {trueG}, {trueB}')

    # 0 is Red, 1 is Green, 2 is Blue
    CurrentPins[0].ChangeDutyCycle(trueR) #ChangeDutyCycle sets the pin value(between 0 and 100); changes the volt of the pin
    CurrentPins[1].ChangeDutyCycle(trueG)
    CurrentPins[2].ChangeDutyCycle(trueB)
    
def setHumanColor(CurrentPins, humancolor): #humancolor is just any color, like 'cyan'
    humancolor = humancolor.lower() # setting humancolor to lower to make sure it can read from the dictionary
    hexColor = colors.CSS4_COLORS.get(humancolor) #CSS4_COLORS is a dictionary of human color keys with values of hex codes
    if hexColor is None:
        print('Color not found')
    else:
        rgbColor = colors.to_rgb(hexColor)
        setColor(CurrentPins=CurrentPins, r = int(rgbColor[0] * 255), g = int(rgbColor[1] * 255), b = int(rgbColor[2] * 255))

# try:
#     while True:
#         inputstr = input('What color would you like to set the lights to? ')
#         setHumanColor(CurrentPins = setPins, humancolor = inputstr)
#         #setColor(setPins, r = int(inputstr.split(',')[0]), g = int(inputstr.split(',')[1]), b = int(inputstr.split(',')[2])) #calling setColor function based on input. It converts inputstr into int, and grabs at respective index
# except:
# 	GPIO.cleanup()


#Relay Code

# GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
# RELAIS_1_GPIO = 15
# GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
# st = time.time()

# try:
	

# 	while time.time() - st < 30: #start time (current time) - time you started while < 30 seconds

# 		GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # off
# 		time.sleep(4)
# 		GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on
# 		time.sleep(4)
# except:
# 	GPIO.cleanup()
