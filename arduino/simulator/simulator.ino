/*
Wattr Project: Arduino Simulation device
by Bryan Marty
*/

const int BUFFER_SIZE = 80;

void setup()                    // run once, when the sketch starts
{
  Serial.begin(9600);
  Serial.flush();
  randomSeed(analogRead(0));
}

int readline(int c, char *buffer, int len) {
  static int pos = 0;
  int rpos;
  
  if (c > 0) {
    switch (c) {
      case '\n':
       rpos = pos;
       pos = 0;
       return rpos;
     default:
     if (pos < len-1) {
       buffer[pos++] = c;
       buffer[pos] = 0;
     }
    }
  }
  return -1;
}

void handlecommand(char *command) {
  String str = String(command);
  if (str == "TEST") {
    Serial.print(millis());
    Serial.print(",");
    Serial.print(random(0,5));
    Serial.print(",");
    Serial.print(random(58,62));
    Serial.println();
    Serial.println("END");
  }
}
  
void loop()
{
  static char buffer[BUFFER_SIZE];
  if(readline(Serial.read(), buffer, BUFFER_SIZE) > 0) {
    //Serial.println(buffer);
    handlecommand(buffer);
  }
}

