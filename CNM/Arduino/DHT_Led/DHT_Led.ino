//2)Thu thập dữ liệu nhiệt độ độ ẩm(DHT)
#include "DHT.h"             //khai báo thư viện DHT
const int DHTPIN = 10;       //Đọc dữ liệu từ DHT11 ở chân 10 trên mạch Arduino
const int DHTTYPE = DHT11;   //Khai báo loại cảm biến, có 2 loại là DHT11 và DHT22
int xanh = 11;
int vang = 12;
int Do = 13;

DHT dht(DHTPIN, DHTTYPE);
 
void setup() {
  pinMode(xanh, OUTPUT);
  pinMode(vang, OUTPUT);
  pinMode(Do, OUTPUT);
  Serial.begin(9600);        //mở cổng serial tại port 9600
  dht.begin();               //Khởi động cảm biến
}
 
void loop() {
  float h = dht.readHumidity();    //Đọc độ ẩm
  float t = dht.readTemperature(); //Đọc nhiệt độ
 
  Serial.print("Nhiet do: ");
  Serial.println(t);               //Xuất nhiệt độ

  if(t<20){
    digitalWrite(vang, HIGH);  
  }else if(t>=20 && t<=27){
    digitalWrite(xanh, HIGH);
  }else {
    digitalWrite(Do, HIGH);
  }

  Serial.print("Do am: ");
  Serial.println(h);               //Xuất độ ẩm
                                  
  Serial.println();               //xuống hàng 
  delay(1000);                     //Đợi 1 giây
}
