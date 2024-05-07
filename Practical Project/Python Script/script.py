import serial
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hahalollmao321",
    database="iot_data"
)
cursor = mydb.cursor()

ser = serial.Serial('/dev/tty.usbmodem11201', 9600)

try:
    while True:
       
        data = ser.readline().decode().strip()
        print("Received data:", data)
        temperature, humidity = data.split(',')
        

        sql = "INSERT INTO sensor_readings (temperature, humidity) VALUES (%s, %s)"
        val = (temperature, humidity)
        cursor.execute(sql, val)
        mydb.commit()

except KeyboardInterrupt:
    ser.close()
    cursor.close()
    mydb.close()
