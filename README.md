# RaspberryPi-Control
Code to play videos and audios using RaspberryPi

## How to use

### Download the MediaControl.py file
### In the code change the following places.

* MQTT broker details

Add the host value (ex : io.adafruit.com) and PORT valu(ex : 1883)
```
HOST = ''
PORT = ''
```

* WiFi credentials

Add the values for the following places to connect the client to the WiFi

```
USERNAME = ''
PASSWORD = ''
```
* Playing media files

'on_message' function will consume the requests coming from the MQTT broker. For your convenience there are couple of entries to play a video and to view an image depending on the request.



### Run the python script by executing the following command in the terminal.

```
python MediaControl.py
```
