import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import os

HOST = 'io.adafruit.com'
PORT = 1883
USERNAME = '' #add the username of the WiFi
PASSWORD = '' # add the password for the WiFi


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("") ## place the MQTT broker path to connect. E.x. : akshika47/feeds/onoff


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    command = str(msg.payload)
    
    ## used to play a clip(audio or video) using omxplayer. The MQTT broker sents 'playvideo1' as the message
    if(command == "playvideo1"):
        os.system('omxplayer -o hdmi 1.wav')

    ## used to display an image. The MQTT broker sents 'displayimage1' as the message
    if(command == "displayimage1"):
        os.system('sudo fbi -T 2 1.png')

client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.connect(host=HOST, port=PORT)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()