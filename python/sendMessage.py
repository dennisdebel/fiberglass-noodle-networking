import sys
import serial
import time


#import morsealf
#import sys


ser = serial.Serial('/dev/cu.usbserial-A7007dlB', 9600) # Establish the connection on a specific port
#counter = 32 # Below 32 everything in ASCII is gibberish

time.sleep(0.5)

#while True:
	#counter +=1
#ser.write("HELLO_\n") # Convert the decimal number to ASCII then send it to the Arduino
	#print ser.readline() # Read the newest output from the Arduino


time.sleep(0.5)
while 1:
	

	var = raw_input("> ")
	
	
	var = var+"_"
#ser.write('\n')
	#print var
   	#print ser.readline()
   	var = var.replace (" ", "-") #replace letter/word space with dash (underscore used for printing serial newlines)
   	ser.write(var.upper())
	#ser.write(var.upper())
#ser.write('\n')

	ser.write('\n')

   	#ser.write("\r\n")
   	time.sleep(5)
   	#print "done"
# data = ser.readline()
# print data
# time.sleep(5)




