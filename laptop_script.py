import psutil
import serial
import time


mySerial = serial.Serial("COM7", baudrate=9600,timeout=1)

upper_limit = 60
lower_limit = 50


while 1:
    battery = psutil.sensors_battery()
    
    if battery.percent >= upper_limit and battery.power_plugged:
        print("charger turned off")
        print(battery.percent)
        mySerial.write(b'0')
    
    elif battery.percent < lower_limit and not battery.power_plugged:
        print("charger turned on")
        print(battery.percent)
        mySerial.write(b'1')

    time.sleep(10)
    



