int led_pin = 13;

void setup() {
  pinMode(led_pin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char cmd = Serial.read();
    if (cmd == '1') {
      digitalWrite(led_pin, HIGH); // LED ON
    } 
    else if (cmd == '0') {
      digitalWrite(led_pin, LOW); // LED OFF
    }
  }
}
