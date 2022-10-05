int MQ2pin = 0;  // khai báo chân kết nối Aout = A0
int buzzer = 10; // khai báo chân 10 của còi
int led = 11;    // khai báo chân 11 của led
int Value;
int nguong_canh_bao = 400;

void setup()
{
  pinMode(led, OUTPUT);    // thiết đặt chân ledPin là OUTPUT
  pinMode(buzzer, OUTPUT); // thiết lập chân còi là OUTPUT
  pinMode(MQ2pin, INPUT);  // chân kết nối Aout = A0
  Serial.begin(9600);      // Mở cổng Serial tại port 9600
}
void loop()
{
  Value = analogRead(MQ2pin);//Đọc giá trị analog tại chân MQ2pin
  //đọc giá trị điện áp ở chân Analog A0, còn ở chân Digital(chân bth) là DigitalRead()
  Serial.print("Gia tri cam bien tai A0: " + Value);// Xuất giá trị đọc được ra serial

  if (Value > nguong_canh_bao)
  {
    Serial.print("Gia tri vuot nguong canh bao !!!\n");
    digitalWrite(led, HIGH); // bật sáng đèn led nối với chân số 11 trên mạch
    tone(buzzer, 1000, 200); // bật còi báo động, 1000 là tần số vuông,
                             // 200 là t/g phát báo động(0,2s)
  }
  else
  {
    Serial.print("Gia tri on dinh ...\n");
    digitalWrite(led, LOW); // den tat
    noTone(buzzer);         // tắt còi báo động
  }
  delay(1000); // tg chờ giữa những lần phát
}