void setup() {
  Serial.begin(9600);
}

void loop() {
  int i = 0;
  Serial.print("#");//区切り文字として
  for (i = 0; i < 10; i++) {
    Serial.print("HelloSerialMonitor!");
  }
}
