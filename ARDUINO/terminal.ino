void setup(){
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  }

void loop(){
  digitalWrite(LED_BUILTIN, HIGH);
  Serial.print("Activado enm 1 logico");
  
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  Serial.print("Cero logico");
  delay(1000);
  }
