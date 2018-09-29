int analogPin = 0;
int value = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop()
{
    char request = ' ';
    if(Serial.available())
    {
      request = Serial.read();
      if(request == '1'){
        digitalWrite(13, HIGH);
      }
      if(request == '0'){
        digitalWrite(13, LOW);
      }
    }
    value = analogRead(analogPin);
    Serial.println(value);
    delay (500);
}



