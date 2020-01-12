void setup() {
  Serial.begin(115200);
}

void loop() { 
  Serial.write(0x17);
  delay(1000);  
}
