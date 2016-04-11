#Fiber Glass Noodle Networking
Proof of concept code for transmitting data (morse) through glass-noodles, using python and arduino.

###Needed
-computer (or two)  
-two ardiunos  
-LDR  
-ultra bright LED or laser diode  

###Quickstart

####Hardware
Align LED and LDR in between a glass noodle.

####Arduino
Copy the 'Morse' folder found in Arduino/libraries to your ~/Documents/Arduino/Libraries folder.
Write ArduinoSend and ArduinoRead to your arduinos.  
Read the max ldr value in the room, fill it in in read_ldr+convert_to_dots.ino (if you only get dots, its to high).  
####Python  
Adjust serial porst of your arduino boards in readMessage.py and sendMessage.py.  
Open two terminals and run readMessage.py in one and sendMessage.py in the other.  
In sendMessage.py a cursor ''>'' will appear, this means you can type a message, hit [enter] key to send it.  
