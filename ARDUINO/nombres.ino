#include<SoftwareSerial.h>
SoftwareSerial will(10,11);
void setup(){
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  will.begin(9600);
  }

void loop(){
  will.println("test");
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  Serial.println("test123");
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
  }
