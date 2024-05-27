import serial
import mysql.connector
import time

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="iot_data"
)
cursor = mydb.cursor()

ser = serial.Serial('/dev/tty.usbmodem11201', 9600)

    # Send pin number and state to Arduino
def send_command(pin, state):
    ser.write(f"{pin},{state}\n".encode())
    
    # Monitor tempreture and humidty readings from sensor and execute conditional statements.
def check_thresholds():

    # Query the most recent temperature and humidity values from the database
    cursor.execute("SELECT temperature, humidity FROM sensor_readings ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    if result:
        temperature, humidity = result
        print("Current temperature:", temperature, "°C")
        print("Current humidity:", humidity, "%")
        
        threshold_temperature = 20.0
        threshold_humidity = 50.0
        
        # 1 = ON, 0 = OFF
        # This sections checks the following conditions and calls send_command function to each pin.
        if temperature > threshold_temperature and humidity > threshold_humidity:

            send_command(3, 1)
            send_command(10, 1)
            print("Temperature and humidity exceed thresholds! LED and buzzer activated")
            
        elif temperature > threshold_temperature:
    
            send_command(3, 1)
            send_command(10, 0)
            print("temperature exceeds threshold LED activated")
            
        elif humidity > threshold_humidity:
            
            send_command(3, 1)
            send_command(10, 1)
            print("humidity exceeds threshold! Buzzer activated")
        else:
            
            send_command(3, 0)
            send_command(10, 0)
            print("temperature and humidity are within acceptable ranges")
    else:
        print("no sensor data found")

try:
    while True:
        check_thresholds()
        time.sleep(5)
except KeyboardInterrupt:
    print("exiting program")
    cursor.close()
    mydb.close()
