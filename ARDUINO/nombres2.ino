#include<SoftwareSerial.h>
SoftwareSerial test(10,11); //rx,tx
void setup(){
  pinMode(LED_BUILTIN, OUTPUT);
  test.begin(9600);
  Serial.begin(9600);
  }

void loop(){
  test.println("admin");
  Serial.println("admin123");
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  
  test.println("ADMIN");
  Serial.println("ADMIN456");
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
  }
