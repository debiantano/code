const int pinTrigger = 2;
const int pinEcho = 3;
const int pinLed = 4;
const int pinBuzzer = 5;

float tiempo=0;
float distancia=0;

void setup()
{
	pinMode(pinTrigger,OUTPUT);
  	pinMode(pinEcho,INPUT);
	pinMode(pinLed,OUTPUT);
	pinMode(pinBuzzer,OUTPUT);
//  	Serial.begin(9600);
}

void loop()
{
	digitalWrite(pinTrigger,LOW);
  	delayMicroseconds(4);
  	digitalWrite(pinTrigger,HIGH);
  	delayMicroseconds(10);
  	digitalWrite(pinTrigger,LOW);
  	tiempo=pulseIn(pinEcho,HIGH);
  	distancia=0.0172*tiempo;
//  	Serial.println("Distancia (cm)");
//  	Serial.println(distancia);
//  	delay(500);
  
  if(distancia>100){
  	noTone(pinBuzzer);
    digitalWrite(pinLed,LOW);
  }
  else{
  	tone(pinBuzzer,1000);
    digitalWrite(pinLed,HIGH);
    delay(distancia*10);
    noTone(pinBuzzer);
    digitalWrite(pinLed,LOW);
    delay(distancia*10);
  }
}
