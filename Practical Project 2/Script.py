import serial
import paho.mqtt.client as paho
import time

ser = serial.Serial('/dev/tty.usbmodem11201', 9600)
print(ser)

def on_publish(client, userdata, result):
    print("Data published to ThingsBoard")

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")

client1 = paho.Client(client_id="tOHcQXIUUUcOyrF6FFti")
client1.on_publish = on_publish
client1.on_connect = on_connect
client1.username_pw_set('tOHcQXIUUUcOyrF6FFti')
client1.connect("thingsboard.cloud", 1883, keepalive=60)

tempThreshold = 30.0
humidityThreshold = 50.0

while True:
    try:
        data = ser.readline().decode().rstrip()
        temperature_str, humidity_str = data.split(',')
        temperature = float(temperature_str)
        humidity = float(humidity_str)
        
        payload = '{{"Temperature": {0}, "Humidity": {1}}}'.format(temperature, humidity)
        client1.publish("v1/devices/me/telemetry", payload)
        print("Device telemetry updated")
        print(payload)
        
        if temperature > tempThreshold:
            ser.write(b'LED_ON\n')
        else:
            ser.write(b'LED_OFF\n')
        
        if humidity > humidityThreshold:
            ser.write(b'BUZZER_ON\n')
        else:
            ser.write(b'BUZZER_OFF\n')
        
    except ValueError as e:
        print(f"Error parsing data: {e}")
    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    time.sleep(5)

