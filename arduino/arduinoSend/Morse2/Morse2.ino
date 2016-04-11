#include <SoftwareSerial.h>

// Author Erik Linder
// Released 2011 under GNU GPLv3
//
// Usage: morse( <pin number>, <speed WPM>, <1=beep, 0=PTT> )
//        sendmsg( "<text-to-send>" )
//

#include <Morse.h>

// Uncomment to beep a speaker at pin 9
//Morse morse(9, 12, 1);
int led = 13;

// Use pin 13 (built-in LED of Arduino 2009)
Morse morse(13, 1, 0);

// Buffer to store incoming commands from serial port
String inData;



void setup()
{
  Serial.begin(9600);
  // Nothing here for the Morse lib
 // Serial.println("Waiting for message...\n"); //otherwise keeps on sending dots...wtf
}

void loop()
{
  
  while(Serial.available() > 0) {
     
    char recieved = Serial.read();
        inData += recieved; 
   // Process message when new line character is recieved
        if (recieved == '\n')
        {
            //Serial.print("Arduino Received: ");
          //Serial.println();
           // Length (with one extra character for the null terminatorNO! that cuases random chars to end up in char)
     int str_len = inData.length(); 

// Prepare the character array (the buffer) 
      char char_array[str_len];

      // Copy it over ...hack
      inData.toCharArray(char_array, str_len);
      morse.sendmsg(char_array);
 // blink 200ms ACK! after sending
  digitalWrite(led, HIGH);   
  delay(200);               
  digitalWrite(led, LOW);    
  delay(200);             
              
      

          //char msg[] = "lol_";
           //  morse.sendmsg(msg);
      //delay (50);

            
     
           // Serial.print(inData);
          // String inData =  String('inData'); 
          // Serial.print(inData);
          //String lol = inData;
          //Serial.print(lol);

          //char msg[] = "lol_";
           //  morse.sendmsg(msg);
          //  Serial.println();
            //delay (2000);
           
            inData = ""; // Clear recieved buffer
        }
    }
 // Serial.println();
//  morse.sendmsg("A");
//  Serial.println("RESPONSE");
//  delay (2000);
//  morse.send(83);
//  morse.send(77);
//  morse.send(48);
//  morse.send(82);
//  morse.send(86);
//  morse.send(86);
  //delay (2000);
}
