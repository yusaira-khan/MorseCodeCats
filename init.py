#!/usr/bin/python

def arduinoSerilizer(buffer):
	import serial #pip install pySerial
	serializer = serial.Serial('COM3', 9600) #/dev/tty.usbserial, is used on Linux

	while 1:
		buffer.append(ser.readline()) #Use this command anytime you want to get an update
