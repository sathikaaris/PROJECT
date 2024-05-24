import time

print(time.strftime("%H:%M"))
alarm_time = input("Enter the Alarm TIme(%H:%M):")
while time.strftime("%H:%M") != alarm_time:
    time.sleep(1)
print ("time to wake_up!")
