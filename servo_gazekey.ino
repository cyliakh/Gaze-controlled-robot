#include <Servo.h>
int incomingByte;

Servo myservo;

int pos;

void setup() {
   Serial.begin(9600);   
}

void loop() {
  // put your main code here, to run repeatedly:
if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    if (incomingByte == 'G'){
      pos = 120;
      myservo.attach(9);
      myservo.write(pos);
      delay(100);
    }
    if (incomingByte == 'W'){
      pos = 30;
      myservo.attach(6);
      myservo.write(pos);
      delay(100);
    }
    if (incomingByte == 'Y'){
      pos = 90;
      myservo.attach(11);
      myservo.write(pos);
      delay(100);
    }
    if (incomingByte == 'Z'){
      pos = 90;
      myservo.attach(10);
      myservo.write(pos);
      delay(100);
    }
//----------------------------------------------------------------------------------------------------------------
    
    if (incomingByte == 'A'){
      delay(100);
     if (pos < 0){
      for (pos = pos; pos <= 0; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
     }
     }
     if (pos > 0){
       for (pos = pos; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
     myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
      }
     }
     pos = 0;
    }
    if (incomingByte == 'B'){
      delay(100);
     if (pos < 30){
      for (pos = pos; pos <= 30; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
     }
     }
     if (pos > 30){
       for (pos = pos; pos >= 30; pos -= 1) { // goes from 180 degrees to 0 degrees
     myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
      }
     }
     pos = 30;
    }
    if (incomingByte == 'C'){
      delay(100);
          if (pos < 60){
      for (pos = pos; pos <= 60; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
     }
     }
     if (pos > 60){
       for (pos = pos; pos >= 60; pos -= 1) { // goes from 180 degrees to 0 degrees
     myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
      }
     }
     pos = 60;
    }
    if (incomingByte == 'D'){
      delay(100);
      if (pos < 90){
      for (pos = pos; pos <= 90; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
     }
     }
     if (pos > 90){
       for (pos = pos; pos >= 90; pos -= 1) { // goes from 180 degrees to 0 degrees
     myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
      }
     }
     pos = 90;
    }
    if (incomingByte == 'E'){
      delay(100);
      if (pos < 120){
      for (pos = pos; pos <= 120; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
     }
     }
     if (pos > 120){
       for (pos = pos; pos >= 120; pos -= 1) { // goes from 180 degrees to 0 degrees
     myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
      }
     }
     pos = 120;
    }
    if (incomingByte == 'F'){
      delay(100);
      if (pos < 150){
      for (pos = pos; pos <= 150; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
     }
     }
     if (pos > 150){
       for (pos = pos; pos >= 150; pos -= 1) { // goes from 180 degrees to 0 degrees
     myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
      }
     }
     pos = 150;
    }
    if (incomingByte == 'H'){
      delay(100);
      if (pos < 180){
      for (pos = pos; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
     }
     }
     if (pos > 180){
       for (pos = pos; pos >= 180; pos -= 1) { // goes from 180 degrees to 0 degrees
     myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
      }
     }
     pos = 180;
    }
    while (Serial.available() >0)
        Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
 }
}
