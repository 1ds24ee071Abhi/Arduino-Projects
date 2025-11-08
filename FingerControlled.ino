// Finger Count LED Controller

int leds[] = {2, 3, 4, 5};
int count;

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 4; i++) {
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], LOW);
  }
}

void loop() {
  if (Serial.available() > 0) {
    count = Serial.read() - '0';
    for (int i = 0; i < 4; i++) {
      if (i < count)
        digitalWrite(leds[i], HIGH);
      else
        digitalWrite(leds[i], LOW);
    }
  }
}
