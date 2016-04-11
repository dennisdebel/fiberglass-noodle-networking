 # -*- coding: utf-8 -*-
import time
import serial
import sys
import io

# def readline(self):
#     eol = "\n"
#     leneol = len(eol)
#     line = bytearray()
#     while True:
#         c = self.ser.read(1)
#         if c:
#             line += c
#             if line[-leneol:] == eol:
#                 break
#         else:
#             break
#     return bytes(line)

# def readline(self, size=None, eol="\n"):
#     """\
#     Read a line which is terminated with end-of-line (eol) character
#     ('\n' by default) or until timeout.
#     """
#     leneol = len(eol)
#     line = bytearray()
#     while True:
#         line += port.read(1)
#         if line[-leneol:] == eol:
#             break
#         if size is not None and len(line) >= size:
#             break
#     return bytes(line)





ser = serial.Serial('/dev/cu.usbserial-A7006wZ6', 9600) # Establish the connection on a specific port, the timeout helps to push data out that might remain in the pipe line..off but gives a newline every n times
#enforce reset befor starting
# ser.setDTR(1)
# time.sleep(0.25)
# ser.setDTR(0)




morseDict = {
   # '\r'           : '\n',
     '._'            : 'A' ,
     '_...'        : 'B' ,
     '_._.'        : 'C' ,
     '_..'          : 'D' ,
     '.'              : 'E' ,
     '.._.'        : 'F' ,
     '__.'          : 'G' ,
     '....'        : 'H' ,
     '..'            : 'I' ,
     '.___'        : 'J' ,
     '_._'          : 'K' ,
     '._..'        : 'L' ,
     '__'            : 'M' ,
     '_.'            : 'N' ,
     '___'          : 'O' ,
     '.__.'        : 'P' ,
     '__._'        : 'Q' ,
     '._.'          : 'R' ,
     '...'          : 'S' ,
     '_'              : 'T' ,
     '.._'          : 'U' ,
     '..._'        : 'V' ,
     '.__'          : 'W' ,
     '_.._'        : 'X' ,
     '_.__'        : 'Y' ,
     '__..'        : 'Z' ,
     '.__._'      : 'Å' ,
     '._._'        : 'Ä' ,
     '___.'        : 'Ö' ,
     '.._..'      : 'É' ,
     '__.__'      : 'Ñ' ,
     '__.__'      : 'Ñ' ,
     '..__'        : 'Ü' ,
     '..__'        : 'Û' ,
     '____'        : 'CH',
     '____'        : 'Š' ,
     '...__..'  : 'ß' ,
     '_._..'      : 'Ç' ,
     '_._..'      : 'Ŝ' ,
     '.____'      : '1' ,
     '..___'      : '2' ,
     '...__'      : '3' ,
     '...._'      : '4' ,
     '.....'      : '5' ,
     '_....'      : '6' ,
     '__...'      : '7' ,
     '___..'      : '8' ,
     '____.'      : '9' ,
     '_____'      : '0' ,
     '..__..'    : '?' ,
     '..__.'      : '!' ,
     '__..__'    : ',' ,
     '._._._'    : '.' ,
     '_..._'      : '=' ,
     '_...._'    : '-' ,
     '_.__.'      : '(' ,
     '_.__._'    : ')' ,
     '........': ' ' ,
     '._._.'      : '+' ,
     '..._._'    : 'Æ' ,
     '.__._ .'    : '@' ,
     '_.._.'      : '/' ,
     '.__..'      : '%' ,
     '._.._.'    : '"' ,
     '_._._.'    : ';' ,
     '___...'    : ':' ,
     '..._.'      : '§' ,
     '.._._'      : '¿' ,
     '_._._'      : '~' ,
     '.____.'    : "_" ,#was: "'", is underscore in arduino code lol!
     '._.._'      : '#' ,
     '._...'      : '&' ,
     '..._.._'  : '$' ,
     '._...'      : '√' ,
     '... .'      : '*' ,
     '__..._'    : '¡' }


l = []	
count = 1


#time.sleep(2) #wait for arduino
while True:
  
	#counter +=1
	#ser.write(str(chr(counter))) # Convert the decimal number to ASCII then send it to the Arduino
     #print ser.readline() # Read the newest output from the arduino
     #byte = ser.read(size=2)
     #print byte
	
	
#     sys.stdout.write(ser.readline())
#     sys.stdout.flush()


     #for i in range(4):
     data = ser.readline()
     #print data
   

     if data.strip() in morseDict:
          
          for c in morseDict[data.strip()]:
               #print c


               l.append(c)
 
      #print s //replace all under scores whit whitespace..somewherw
               if c == "_":
     #             l.append(" ")
                    s = ''.join(l)
                    s = s.replace("-"," ") #replace letter/word glue dashes with space
                    s = s.replace("_","") #replace newline underscores with nothing
                    print s
                    l = [] #clears the list after each word, line...
     #           l.append(c)
     #                #s = ''.join(l)
     # #print s //replace all under scores whit whitespace..somewherw
     #           if c.isspace() == True:
     #                #l.append(" ")
     #                s = ''.join(l)
     #                print s
     #                l = [] #clears the list after each word, line...
     #           #    s = ''.join(l)
               
     #      else:
     #           print " "


     # for c in ser.read():
          

     #      #if c.isspace():
     #      #     print "empty"
     #      if c.isspace() == False:  #if not newline or space or empty...
     #           l.append(c) #append character in list
     #           joined_l = ''.join(l) #Make a string from array
               
     #           print joined_l
     #      # print("Line " + str(count) + ': ' + joined_l)
         
     #           #for c in morseDict[joined_l]:
     #           #     print c
     #      l = []
     #      count += 1
     #      break


ser.close()
#--------------------------old code
	# #for i in range(4):
 #     data = ser.readline()
 #     print data
   

 #     if data.strip() in morseDict:
          
 #          for c in morseDict[data.strip()]:
 #               print c

 #               l.append(c)
	# 			#s = ''.join(l)
	# #print s //replace all under scores whit whitespace..somewherw
 #               if c == "_":
	# 			#l.append(" ")
 #                    s = ''.join(l)
 #                    print s
 #                    l = [] #clears the list after each word, line...
	# 		#	s = ''.join(l)
			
	# 	else:
	# 		print " "
		
		#sys.stdout.write(data.rstrip('\n\r ')) # Will replace all trailing \n, \r and ' '
		#sys.stdout.write(data.strip('\n\r')) # Will replace >>all<< \n, \r and
		
			
#--------------------------old code		

			
				
				

     #sleep(.1) # Delay for one tenth of a second
     #if counter == 255:
    # 	counter = 32