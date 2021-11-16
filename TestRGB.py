import time
import RPi.GPIO as GPIO
from RaspberryPiPinControl import setrgbGPIO, setColor, setHumanColor
from RedmondForecast import RedmondForecast, WEATHERCOLOR

#GLOBAL VARIABLE
pins = setrgbGPIO()

#Create funcion to get color from WeatherAPI or set color.
def get_set_color():
    forecast = RedmondForecast()
    todayforecast = RedmondForecast()[0]['Weather Desc.']
    forecastcolor = WEATHERCOLOR.get(todayforecast, 'blue')
    setHumanColor(CurrentPins = pins, humancolor = forecastcolor)

if __name__ == '__main__':
    setColor(CurrentPins = pins, r = 255, g = 0, b = 0)

    while True:
        forecast = RedmondForecast()
        todayforecast = RedmondForecast()[0]['Weather Desc.']
        forecastcolor = WEATHERCOLOR.get(todayforecast, 'blue')
        setHumanColor(CurrentPins = pins, humancolor = forecastcolor)
        time.sleep(3600)
        print('Color was refreshed')

    #time.sleep(3)
    #GPIO.cleanup()

    #Switch colors based on CSS input

    # try:
    #     while True:
    #         inputstr = input('What color would you like to set the lights to? ')
    #         setHumanColor(CurrentPins = pins, humancolor = inputstr)
    #         setColor(pins, r = int(inputstr.split(',')[0]), g = int(inputstr.split(',')[1]), b = int(inputstr.split(',')[2])) #calling setColor function based on input. It converts inputstr into int, and grabs at respective index
    # except:
    # 	GPIO.cleanup()
    