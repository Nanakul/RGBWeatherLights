import time
import paho.mqtt.client as mqtt
import sys

client = mqtt.Client()
rgb_lights = open('/home/pi/RGBLights/TestRGB.py', 'r')

if client.connect('nmxo.local', 1883, 60) != 0:
    print('Could not connect to MQTT Broker!')
    sys.exit(-1)

client.publish('Weather', 'WeatherAPI', 0)

client.disconnect()
