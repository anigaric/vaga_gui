char count = 0;
void setup() {
  Serial.begin(115200);
}

void loop() { 
  int i;

 
  Serial.write(0x17);
  delay(10);    
  Serial.write(0xA3);
  delay(10);    
  Serial.write(0x91); 
    delay(10);  
  Serial.write(0xF4);
    delay(10);  

  Serial.write(0x01);
    delay(10);
  Serial.write(count);
    delay(10);
   Serial.write(0x85);
   delay(10);
  for(i=0;i<10;i++){
    Serial.write(0x10);
      delay(10);
    Serial.write(0x20);
      delay(10);
    Serial.write(0x30);
      delay(10);
    Serial.write(0x40);
      delay(10);
    Serial.write(0x10);
      delay(10);
    Serial.write(0x60);
      delay(10);
    Serial.write(0x70);
      delay(10);
    Serial.write(0x80);
      delay(10);
  }
  Serial.write(0x33);
    delay(10);
  Serial.write(0x33);
    delay(10);
  Serial.write(0x44);
    delay(10);
  Serial.write(0x44);
    delay(10);
  Serial.write(0x99);
    delay(10);
  Serial.write(0xFF);
    delay(10);

  count = count + 1;

} 
