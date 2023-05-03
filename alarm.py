import datetime
from playsound import playsound
alarmHour = int(input("Enter hour: "))
alarmMin = int(input("Enter minutes: "))
alarmAm = input("am / pm:")

if alarmAm=="pm":
    alarmHour+=12

while True:
    if alarmHour==datetime.datetime.now().hour and alarmMin==datatime.now().minute:
        print("playing..")
        playsound("punky.mp3")
        break
 
