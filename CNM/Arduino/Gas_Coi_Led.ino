//int MQ2pin = A0;       //khai báo chân kết nối Aout = A0
int buzzer = 10;      //khai báo chân 10 của còi
int led = 11;         //khai báo chân 11 của led
int Value; 
int nguong_canh_bao = 150;

void setup()
{
  pinMode(led, OUTPUT);
  pinMode(buzzer, OUTPUT);
  //pinMode(MQ2pin, INPUT);
  Serial.begin(9600);           //Mở cổng Serial tại port 9600
}
void loop()
{
  Value = analogRead(A0);      //đọc giá trị điện áp ở chân Analog A0, còn ở chân Digital(chân bth) là DigitalRead()
  Serial.print("Value: ");
  Serial.print(Value);
    
  if(Value > nguong_canh_bao)
  {
    Serial.print("\nGia tri vuot nguong canh bao 150 !!!\n");
    digitalWrite(led, HIGH);
    tone(buzzer, 1000, 200);                   //bật còi báo động, 1000 là tần số vuông, 500 là t/g phát báo động
  }
  else
  {
    Serial.print("\nGia tri on dinh ...\n");
    digitalWrite(led, LOW);
    noTone(buzzer);                            //tắt còi báo động

  }
  delay(1000); 
}
