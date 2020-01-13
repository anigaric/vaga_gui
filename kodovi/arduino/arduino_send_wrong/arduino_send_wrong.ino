void setup() { 
  Serial.begin(115200);
  
}

void loop() { 
    byte header[] = {0x17, 0xA3, 0x91, 0xF4};
  byte rest[] = {0x01, 0x23, 0x85};
  byte rest2[] = {0x33, 0x33, 0x44, 0x44, 0x99, 0xFF};
  int i, a, b, c; 
  
	for(a=0; a<4; i++){
		Serial.write(header[a]);
		delay(500);
	}

	for(b=0; b<3; i++){
		Serial.write(rest[b]);
		delay(500);
	}

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

	for(c=0; c<6; i++){
		Serial.write(rest2[c]);
		delay(500);
	}

} 
