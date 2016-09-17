boolean up;
int speed;

void setup() {
  Serial.begin(9600);
  speed = 0;
  up = true;
}

void loop() {
  if(up){
    speed+=50;  
    if(speed >= 255){
      up = false;  
    }
  } else{
    speed-=50;
    if(speed <= 0){
      up = true;
    }
  }

  
  analogWrite(5, speed);
  Serial.print(speed);
  Serial.print("\n");
  delay(2000);
}
