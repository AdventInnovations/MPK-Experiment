int rgb_blue = 2;
int rgb_green = 3;
int rgb_red = 4;
int blue = 8;
int red = 7;
int green = 6;
int diode_sensor = A0;
int transistor_sensor = A2;

bool send_diode_data = false;
bool send_transistor_data = false;
String cmd;
String color;
String val;

void setup() {
  for (int i = 2; i<=8;i++)
  {
    pinMode(i, OUTPUT);
  }
  

  Serial.begin(115200);
  
  setRGB(0, 0, 0);
  digitalWrite(red, LOW);
  digitalWrite(green, LOW);
  digitalWrite(blue, LOW);


}

void loop() {
  
  if (Serial.available())
  {

    cmd = Serial.readStringUntil(' ');
    

    if (cmd == "set")
    {
      color = Serial.readStringUntil(' ');
      val = Serial.readStringUntil(' ');
      if (color == "rgb_blue")
      {
        setRGB(0, 0, val.toInt());
      }
      else if (color == "rgb_red")
      {
        setRGB(val.toInt(), 0, 0);
      }
      else if (color == "rgb_green")
      {
        setRGB(0, val.toInt(), 0);
      }
      else if (color == "blue")
      {
        digitalWrite(blue, val.toInt());
      }
      else if (color == "red")
      {
        digitalWrite(red, val.toInt());
      }
      else if (color == "green")
      {
        digitalWrite(green, val.toInt());
      }
    }
    else if (cmd == "start_diode")
    {
      send_transistor_data = false;
      send_diode_data = true;
    }
    else if (cmd == "start_transistor")
    {
       send_transistor_data = true;
      send_diode_data = false;
    }
    else if (cmd == "stop")
    {
      send_transistor_data = false;
      send_diode_data = false;
    }
    
  }

  if (send_diode_data)
  {
    Serial.println(analogRead(diode_sensor));
  }
  else if (send_transistor_data)
  Serial.println(analogRead(transistor_sensor));
  cmd = "";
  val = "";
  color = "";
}

void setRGB(int R, int G, int B)
{
  analogWrite(rgb_red, 255 - R);
  analogWrite(rgb_green, 255 - G);
  analogWrite(rgb_blue, 255 - B);
}
