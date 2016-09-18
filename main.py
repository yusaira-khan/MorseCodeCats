#!/usr/bin/python

from threading import Thread,Event
import time
import os
import sys
import signal
from db import *
import serial #pip install pySerial

def arduinoSerilizer(buffer,event):
	serializer = serial.Serial('/dev/tty.usbmodem1421', 9600) #/dev/tty.usbserial, is used on Linux

	while event.is_set():
		buffer.append(serializer.readline()) #Use this command anytime you want to get an update
	else:
		serializer.close()

# def translate(rawData):
# 	#Query database for rawData
# 	translatedData = 5#query
# 	return translatedData

def log(transData):
	#Insert into table datetime and transData
	pass


buffer = []
event=Event()
event.set()
thread = Thread(target=arduinoSerilizer, args=(buffer,event))
thread.daemon = True
thread.start()

#DO your stuff here
letter = getRandomLetter()
print("What is the correct morse code for '"+letter+"' ?\n")
def writeS(num):
	serializer = serial.Serial('/dev/tty.usbmodem1421', 9600)
	serializer.write(int(num))

try:
	while 1:
		try:
			x = buffer.pop(0)
			break
		except:
			pass
	if x[-1] == '\r' or x[-1] == '\n':
		code = x[:-1]
	if code[-1] == '\r' or code[-1] == '\n':
		code = code[:-1]
	correctness=isCorrectCode(letter,code)
	if(correctness):
		print "You are a CAT!"
	else:
		print "You're not a cat. Go *** yourself"
	writeS(correctness)
	#print("Received: {}, Translated: {}".format(code, code))
	event.clear()
	#thread.join()
	#print "woo"
	sys.exit()		#time.sleep(1)
except Exception as e:
	print str(e)
