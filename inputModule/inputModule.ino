//Buffer Array object
#define ConnectThreshold 900 //V
#define DisconnectThreshold 400 //V

#define ShortCycles  1 //3*100
#define LongCycles 5 //10*100
#define Cycle 50 //ms
#define SpaceCycles 100 //1 char/5s

class BufferArray {
  public:
    BufferArray() {}
    int buff[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int state = 0;

    void updateArray(int newValue) {
      state++;
      if (state >= 10) {
        state = 0;
      }
      buff[state] = newValue;
    }
    int averageArray() {
      int sum = 0;
      for (int i = 0; i < 10; i++) {
        sum = sum + buff[i];
      }
      return sum / 10;
    }

};

void LEDIndicator(int hold) {
  if (hold >= ShortCycles && hold < LongCycles) {
    analogWrite(5, 100);
  }
  else if (hold >= LongCycles) {
    analogWrite(5, 250);
  }
  else {
    analogWrite(5, 0);
  }
}

void AnalyseSerial(){
  if(Serial.available()>0){ //Messages inbound
    int incoming = Serial.read();
    if(incoming == 0){ //Got a question wrong
      analogWrite(6, 255);
      delay(40);
      analogWrite(6,0);
    }
  }
}
//MAIN CODE

BufferArray* buff;
int holdDuration, charPeriod;

void setup() {
  Serial.begin(9600);
  buff = new BufferArray();
  holdDuration = 0;
  charPeriod = 0;
}

void loop() {
  int start = millis();

  buff->updateArray(analogRead(0));
  int readValue = analogRead(0);
  //  int readValue = buff->averageArray();

  if (readValue > ConnectThreshold) { //Pushed
    if(charPeriod==0){charPeriod++;}
    holdDuration++;

  } else {
    if (readValue < DisconnectThreshold) { //Released
      if (holdDuration >= ShortCycles && holdDuration < LongCycles) { //Short
        Serial.write(".");
      } else {
        if (holdDuration >= LongCycles) { //Long
          Serial.write("-");
        }
      }
      holdDuration = 0;
      //Reset caclulators and output whether it was short or long
    }
  }

  if(charPeriod-1>=SpaceCycles){ //Off by 1 error
    Serial.println();
    charPeriod=0;
  }
  if(charPeriod>0){ charPeriod++; }

  LEDIndicator(holdDuration);
  AnalyseSerial();

  //Make sure ticks are regular and non negative.
  int delayTime = Cycle - (millis() - start);
  if (delayTime < 0) delayTime = 0;
  delay(delayTime);
}
