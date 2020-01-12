void setup() {
  Serial.begin(115200);
}

void loop() { 
  Serial.write(0x06);
  delay(1000);    
  Serial.write(0x29);
  delay(1000);    

} 
