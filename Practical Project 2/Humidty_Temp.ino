#include <DHT.h>

#define DHTPIN 7
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

#define LED_PIN 3
#define BUZZER_PIN 4

float tempThreshold = 30.0;
float humidityThreshold = 50.0;

void setup() {
  Serial.begin(9600);
  dht.begin();

  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
}

void loop() {
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  Serial.print(temperature);
  Serial.print(",");
  Serial.print(humidity);
  Serial.println();

  if (temperature > tempThreshold && humidity > humidityThreshold) {
  
    for (int i = 0; i < 10; i++) {
        digitalWrite(LED_PIN, HIGH); 
        digitalWrite(BUZZER_PIN, HIGH); 
        delay(500); 
        digitalWrite(LED_PIN, LOW); 
        digitalWrite(BUZZER_PIN, LOW); 
        delay(500); 
    }
    exit(0); 
  } else if (temperature > tempThreshold) {
   
    for (int i = 0; i < 10; i++) {
        digitalWrite(LED_PIN, HIGH); 
        delay(500); 
        digitalWrite(LED_PIN, LOW); 
        delay(500); 
    }
    exit(0); 
  } else if (humidity > humidityThreshold) {
   
    for (int i = 0; i < 10; i++) {
        digitalWrite(BUZZER_PIN, HIGH); 
        delay(500); 
        digitalWrite(BUZZER_PIN, LOW); 
        delay(500); 
    exit(0);
    } 

  } else {

    digitalWrite(LED_PIN, LOW); 
    digitalWrite(BUZZER_PIN, LOW); 
  }

  delay(2000);
}
