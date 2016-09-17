//Buffer Array object
#define ConnectThreshold 900
#define DisconnectThreshold 400
#define ShortDuration  300
#define LongDuration 1000

class BufferArray{
  public:
    BufferArray(){}
    int buff[10] = {0,0,0,0,0,0,0,0,0,0};
    int state = 0;

    void updateArray(int newValue){
      state++;
      if(state>=10){ state = 0; }
      buff[state] = newValue;
    }
    int averageArray(){
      int sum = 0;
      for(int i=0; i<10; i++){ sum = sum + buff[i]; }
      return sum/10;
    }
  
};


//MAIN CODE

int readVal;
BufferArray* buff;

void setup() {
  Serial.begin(9600);
  readVal = 0;
  buff = new BufferArray();
}

void loop() {
  buff->updateArray(analogRead(0));

  
  Serial.println(buff->averageArray());
  delay(100);
}
