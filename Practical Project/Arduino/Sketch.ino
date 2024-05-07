#include <DHT.h>

#define DHTPIN 7      
#define DHTTYPE DHT11 

DHT dht(DHTPIN, DHTTYPE);

#define LED_PIN 3
#define BUZZER_PIN 10   


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

  float threshold_temperature = 20.0;
  float threshold_humidity = 50.0;

  
  if (temperature > threshold_temperature && humidity > threshold_humidity) {
    digitalWrite(LED_PIN, HIGH);
    digitalWrite(BUZZER_PIN, HIGH);
    delay(500); 
  } else if (temperature > threshold_temperature) {
    digitalWrite(LED_PIN, HIGH);
    digitalWrite(BUZZER_PIN, LOW);
  } else if (humidity > threshold_humidity) {
    digitalWrite(BUZZER_PIN, HIGH);
    delay(500); 
    digitalWrite(BUZZER_PIN, LOW);
    digitalWrite(LED_PIN, LOW);
  } else {
    digitalWrite(LED_PIN, LOW);
    digitalWrite(BUZZER_PIN, LOW);
  }

  delay(2000);
}
