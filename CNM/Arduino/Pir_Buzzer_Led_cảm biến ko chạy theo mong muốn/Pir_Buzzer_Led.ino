int ledPin = 13;     // chọn chân 13 báo hiệu LED
int inputPin = 2;    // chọn ngõ tín hiệu vào cho PIR
int val = 0;         // chọn ngõ tín hiệu vào cho PIR
int pinSpeaker = 10; // chọn chân cho chuông khi có đột nhập

void setup()
{
  pinMode(ledPin, OUTPUT);
  pinMode(inputPin, INPUT);
  pinMode(pinSpeaker, OUTPUT);
  Serial.begin(9600);
}

// tone(pin, frequency, duration)
// pin: chân kết nối, frequency: tần số sóng vuông,duration: thời gian phát nhạc(mili giây)

void loop()
{
  val = digitalRead(inputPin); // đọc giá trị đầu vào.
  if (val == HIGH)             // nếu giá trị ở mức cao.(1)
  {
    digitalWrite(ledPin, HIGH); // LED On
    playTone(300, 160);         // thời gian còi kêu
    Serial.println("1");        // xuất ra 1 trong tg còi kêu
    delay(1000);
  }
  else
  {
    digitalWrite(ledPin, LOW);
    playTone(0, 0);      // phát nhạc
    Serial.println("0"); // // xuất ra 0 trong tg còi tắt
    delay(1000);
  }
}

void playTone(long duration, int freq) // hàm xuất âm thanh
{
  duration *= 100; // thời gian phát nhạc (đơn vị mili giây)
  int period = (1.0 / freq) * 1000000;
  long elapsed_time = 0;
  while (elapsed_time < duration)
  {
    digitalWrite(pinSpeaker, HIGH); //// giữ trạng thái chân pinSpeaker 10 là HIGH
    delayMicroseconds(period / 2);//Tạm dừng chương trình trong khoảng thời gian 
    digitalWrite(pinSpeaker, LOW);
    delayMicroseconds(period / 2);
    elapsed_time += (period);
  }
}
