void setup() {
  // put your setup code here, to run once:
  pinMode(2,OUTPUT);
  pinMode(7,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    char cmd = Serial.read();
    if(cmd == 'G'){
      digitalWrite(2,HIGH);
      delay(2000);
      digitalWrite(2,LOW);
    }
    else if(cmd == 'R'){
      digitalWrite(7,HIGH);
      delay(2000);
      digitalWrite(7,LOW);
    }
  }
  delay(100);
}
