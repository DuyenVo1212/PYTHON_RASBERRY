#define xanh 2
#define vang 3
#define Do 4
#define Number_led 3
// int xanh=2;

int array[] = {xanh, vang, Do};  // mảng gồm 3 đèn
int on_off[] = {HIGH, LOW};      // khai báo trạng thái bật tắt của đèn
int time[] = {1000, 2000, 3000}; // thời gian đèn sáng lần lượt là xanh 1s,đỏ 2s,vàng 3s

void setup()
{
  for (int i = 0; i < 3; i++)
  {
    pinMode(array[i], OUTPUT); // ban đầu cả 3 đèn đều tắt
  }
}

void loop()
{
  for (int i = 0; i < Number_led; i++) // vòng lặp sáng tắt
  {
    digitalWrite(array[i], on_off[0]); // 3 đèn sáng
    delay(time[i]);
    digitalWrite(array[i], on_off[1]); // 3 đèn tắt
  }
}

// int xanh = 2;
// int vang = 3;
// int Do = 4;
// void setup()
//{
//   pinMode(xanh, OUTPUT);
//   pinMode(vang, OUTPUT);
//   pinMode(Do, OUTPUT);
// }
//
// void loop()
//{
//   digitalWrite(xanh, HIGH);
//   delay(1000);
//   digitalWrite(xanh, LOW);
//
//   digitalWrite(vang, HIGH);
//   delay(1000);
//   digitalWrite(vang, LOW);
//
//   digitalWrite(Do, HIGH);
//   delay(1000);
//   digitalWrite(Do, LOW);
// }
