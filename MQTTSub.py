import paho.mqtt.client as mqtt
import sys
from requests.api import get
from RaspberryPiPinControl import setrgbGPIO, setColor, setHumanColor
from RedmondForecast import RedmondForecast, WEATHERCOLOR
from TestRGB import get_set_color, pins


client = mqtt.Client()

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode()))
    if msg.topic == 'Weather':
        if str(msg.payload.decode()) == 'WeatherAPI':
            get_set_color()
        else:
            setHumanColor(CurrentPins=pins,humancolor=str(msg.payload.decode()))

client.on_message = on_message

if client.connect('nmxo.local', 1883, 60) != 0:
    print('Could not connect to MQTT Broker!')
    sys.exit(-1)

client.subscribe('Weather')

if __name__ == '__main__':

    try:
        print('Press CTRL+C to exit...')
        client.loop_forever()
    except:
        print('Disconnecting from broker...')