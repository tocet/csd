#include<ESP8266WiFi.h>
#include<ESPAsyncTCP.h>
#include<ESPAsyncWebServer.h>

#define BAUDRATE 115200
#define LED_R 12
#define LED_B 14    // buzzer 

const char* ssid = "Laboratorium-IoT";
const char* pass = "IoTL@bolatorium";
AsyncWebServer server(80);

void wifi_connect() {
  WiFi.begin(ssid,pass);
  Serial.print("Connecting .");
  while(WiFi.status()!=WL_CONNECTED) {
    Serial.print(".");
    delay(250);
  }
  Serial.print("\nIP: ");
  Serial.println(WiFi.localIP());
}

void setup() {
Serial.begin(BAUDRATE);
pinMode(LED_B,OUTPUT);
pinMode(LED_R,OUTPUT);
wifi_connect();

//web page
server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
//    request->send_P(200, "text/html", index_html);
      request->send(200, "text/plain", "LED");
  });

server.begin();
}

long p_millis = 0;
int led_state = LOW;
#define DELAY 500

void loop() {

if(millis() - p_millis >= DELAY) {
  led_state = (led_state == LOW)? HIGH:LOW;
  Serial.println("LED state " + String(led_state));
  digitalWrite(LED_R,led_state);
  p_millis = millis();
}

}
