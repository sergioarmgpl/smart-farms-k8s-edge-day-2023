import RPi.GPIO as GPIO
import dht11
import time
import requests
# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
while True:
   instance = dht11.DHT11(pin = 22)
   result = instance.read()

   if result.is_valid():
      print("Temperature: %-3.1f C" % result.temperature)
      print("Humidity: %-3.1f %%" % result.humidity)
      r = requests.post("http://172.16.0.150:3000/device",
      json = { "t":float(result.temperature),
      "h":float(result.humidity),
      "d":1})
   time.sleep(1)
#   else:
#      print("Error: %d" % result.error_code)
