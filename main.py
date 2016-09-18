#!/usr/bin/python
from threading import Thread
import time
from db import *
import signal
import sys
import time
import os

def signal_handler(signal, frame):
    print 'Aah! Too coward to know if you\'re a cat, eh?'
    os._exit(0)

signal.signal(signal.SIGINT, signal_handler)

def arduinoSerilizer(buffer):
	import serial #pip install pySerial
	#serializer = serial.Serial('COM3', 9600) #/dev/tty.usbserial, is used on Linux
	serializer = serial.Serial('/dev/tty.usbmodem1421', 9600) #/dev/tty.usbserial, is used on Linux

	while 1:
		buffer.append(serializer.readline()) #Use this command anytime you want to get an update

def translate(rawData):
	#Query database for rawData
	translatedData = 5#query
	return translatedData

def log(transData):
	#Insert into table datetime and transData
	pass


buffer = []
thread = Thread(target=arduinoSerilizer, args=(buffer,))
thread.start()

#DO your stuff here
print "Welcome to Morse Code cats! Figure out the morse code to see which cat you are!"
#hile 1:
letter = getRandomLetter()
print("What is the correct morse code for '"+letter+"' ?\n")
try:
	x = buffer.pop(0)

	if(x[-1]=='\n'):
		code=x[:-1]
	else:
		code=x

	if(isCorrectCode(letter,code)):
		print "You are a CAT! Try again or Press Ctrl+C to quit"
	else:
		print "You're not a cat. Go *** yourself"
		os._exit(1)

	time.sleep(1)
except:
	pass
	#print("OOPs error!")
	#sys.exit(2)
