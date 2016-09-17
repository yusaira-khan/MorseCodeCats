#!/usr/bin/python
from threading import Thread
import time

def arduinoSerilizer(buffer):
	import serial #pip install pySerial
	serializer = serial.Serial('COM3', 9600) #/dev/tty.usbserial, is used on Linux

	while 1:
		buffer.append(serializer.readline()) #Use this command anytime you want to get an update

def translate(rawData):
	#Query database for rawData
	translatedData = #query
	return translatedData

def log(transData):
	#Insert into table datetime and transData
	pass
		
		
buffer = []
thread = Thread(target=arduinoSerilizer, args=(buffer,))
thread.start()

#DO your stuff here

while 1:
	try:
		x = buffer.pop(0)
		x2 = translate(x)
		log(x2)
		print("Received: {}, Translated: {}".format(x, x2))
		
		time.sleep(1)
	except:
		pass