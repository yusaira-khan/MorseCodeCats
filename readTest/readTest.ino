int readVal;
int[] buff;
int state;

void setup() {
  Serial.begin(9600);
  readVal = 0;
  buff = {0,0,0,0,0,0,0,0,0,0};
  state = 0;
}

void loop() {
  updateArray(analogRead(0));

  
  Serial.println(averageArray);
  delay(100);
}

void updateArray(int newValue){
  state++;
  if(state>=10){ state = 0; }
  int[state] = newValue;
}
int averageArray(){
  int sum = 0;
  for(int i=0; i<10; i++){ sum = sum + buff[i]; }
  return sum;
}

