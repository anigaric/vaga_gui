void setup() {
  Serial.begin(115200);
}

void loop() { 
	int i;
	Serial.write(0x17);
	delay(1000);		
	Serial.write(0xA3);
	delay(1000);		
	Serial.write(0x91);	
		delay(1000);	
	Serial.write(0xF4);
		delay(1000);	

	Serial.write(0x01);
		delay(1000);
	Serial.write(0x23);
		delay(1000);
   Serial.write(0x85);
   delay(1000);
	for(i=0;i<10;i++){
		Serial.write(0x10);
			delay(1000);
		Serial.write(0x20);
			delay(1000);
		Serial.write(0x30);
			delay(1000);
		Serial.write(0x40);
			delay(1000);
		Serial.write(0x50);
			delay(1000);
		Serial.write(0x60);
			delay(1000);
		Serial.write(0x70);
			delay(1000);
		Serial.write(0x80);
			delay(1000);
	}
	Serial.write(0x33);
		delay(1000);
	Serial.write(0x33);
		delay(1000);
	Serial.write(0x44);
		delay(1000);
	Serial.write(0x44);
		delay(1000);
	Serial.write(0x99);
		delay(1000);
	Serial.write(0xFF);
		delay(1000);

} 
