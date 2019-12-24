#define relayPin 7

char x;
void setup() {
  Serial.begin(9600);
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, HIGH);
  
}
void loop() {
  if(Serial.available() > 0){ 
    x = Serial.read();    
 }
 
 if (x == '0') { 
  digitalWrite(relayPin, HIGH);
  x = 0; 
 }
 
 else if (x == '1') {
  digitalWrite(relayPin, LOW);
  x = 0;
 } }
