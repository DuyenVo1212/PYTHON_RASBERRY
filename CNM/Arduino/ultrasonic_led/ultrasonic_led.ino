#define TRIG_PIN 8    // Chân Trig nối với chân 8
#define ECHO_PIN 7    // Chân Echo nối với chân 7
#define TIME_OUT 5000 // Time_out của pulseIn là 5000 microsecond

int xanh = 13;
int vang = 12;
int Do = 10;

// Chương trình con tính khoảng cách
float getDistance(){
  long duration, distanceCm;

  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  
  // Thời gian tín hiệu phản hồi lại chân Echo
  duration = pulseIn(ECHO_PIN, HIGH, TIME_OUT);
 
  // Tính khoảng cách 
  distanceCm = duration / 29.1 / 2;
  
  // trả lại giá trịnh tính được
  return distanceCm;
}
 
void setup() {  
  Serial.begin(9600);
 
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  
  pinMode(xanh,OUTPUT);
  pinMode(vang,OUTPUT);
  pinMode(Do,OUTPUT);
  
  //digitalWrite(13,LOW);
  //digitalWrite(12,LOW);
  //digitalWrite(10,LOW);
}
 
void loop() {
  // gọi chương trình con getDistance
  long distance = getDistance();
 
  if (distance <= 0)    // nếu khoang cach <0
  {
    Serial.println("Dua vat the lai gan !!"); 
  }
  else{
    // Hiển thị khoảng cách đo được lên Serial Monitor   
    Serial.print("Khoang cach do duoc (cm): ");
    Serial.println(distance);
  }
  if(distance <=10 && distance >0 ){
    digitalWrite(13,HIGH);
    digitalWrite(12,LOW);
  }
  else if(distance >10){
    digitalWrite(12,HIGH);
    digitalWrite(13,LOW);
  }
  else{
    digitalWrite(12,LOW);
    digitalWrite(13,LOW);
    digitalWrite(10,LOW);
  }
  delay(1000);
}
