boolean up = true;
int speed = 100;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if(up){
    speed+=5;  
    if(speed >= 255){
      up = false;  
    }
  }

  
  analogWrite(5, speed);
  Serial.print(speed);
  delay(1000);
}
