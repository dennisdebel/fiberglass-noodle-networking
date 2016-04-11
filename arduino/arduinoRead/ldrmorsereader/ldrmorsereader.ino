int LDR_Pin = A2; //analog pin 0
int led = 13;
//Maximum reading from the LDR with laser on.
int LDR_Maxvalue=125; //debug down below. 1010 led ON ldr.  (if only dots: value to high)
int dot_length=10000; //0,9 sec, debug with counter high below
int dash_length=30000;
int letter_pause=30000;

int ack_lenght=1600; // ack after sending letter/line, 2x blink



void setup(){
  Serial.begin(9600);
  pinMode(led, OUTPUT);    
}

int counter_high = 0;
int counter_low = 0;

void loop(){
//   if (( counter_low > 1500) &&( counter_high == 1)) {
//    Serial.println();
//   }



  
  int LDRReading = analogRead(LDR_Pin); 
  //Serial.println(LDRReading);//debug room light
  
  if (LDRReading >= LDR_Maxvalue){
  counter_high++ ;
   if ( counter_low > 0 ){
 //     Serial.print("Low\t");
//      Serial.print("Low\t");
//     Serial.println(counter_low);
//     Serial.print("Hi\t");
//     Serial.println(counter_high);
 //    Serial.print("\n");
     // Serial.println();
   }
   if ( counter_low >= letter_pause) {
    
      Serial.println();
  
  }
    
     counter_low=0;
     digitalWrite(led, HIGH);
    
  
  } else {
//   Serial.print(".");

   
  counter_low++;
  if ( counter_high > 0 ){
//      Serial.print("High\t");  
//   Serial.println(counter_high); // debug timing


  
     //ack code > implemented in morse library for blink after eachh char now (200ms blink)
    if ( (counter_high <= 3000 ) &&( counter_high >= 1600) ){
    Serial.println();
//    Serial.println();

  }

  

  } 
  
  if ( (counter_high <= letter_pause ) &&( counter_high >=dot_length) ){
//      Serial.print(counter_high);
    Serial.print(".");

  }
  if ( counter_high > letter_pause ){
 //         Serial.print(counter_high);
        Serial.print("_");
  }
       
      counter_high=0;
      digitalWrite(led, LOW);

  }





//delay(.1); //wait seemsto help... not needed tho?
 
}



