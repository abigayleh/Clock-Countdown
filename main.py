import time
import os

clock = False
countDown = False

operation = input("Clock or Countdown")
if operation.lower() == "clock":
    clock = True
elif operation.lower() == "countdown":
    countDown = True
seconds = int(input("Enter seconds"))
while 59 < seconds < 0:
    seconds = int(input("Invalid input, please enter seconds"))
minutes = int(input("Enter minutes"))
while 0 < minutes > 59:
    minutes = int(input("Invalid input, please enter minutes"))
hours = int(input("Enter hours"))
while 0 < hours > 23:
    hours = int(input("Invalid input, please enter hours"))

while clock:
    os.system('cls')
    print(str(hours).zfill(2), ":", str(minutes).zfill(2), ":", str(seconds).zfill(2))
    seconds = (seconds + 1)
    time.sleep(1)
    if hours == 23 and minutes == 59 and seconds == 59:
        hours = -1
    if minutes == 59 and seconds == 59:
        minutes = -1
        hours += 1
    if seconds == 59:
        seconds = -1
        minutes += 1
    if seconds < 10:
        seconds = int("0" + str(seconds))

while countDown:
    os.system('cls')
    print(str(hours).zfill(2), ":", str(minutes).zfill(2), ":", str(seconds).zfill(2))
    seconds = (seconds - 1)
    time.sleep(1)
    if hours == 0 and minutes == 0 and seconds == 0:
        print("Timer complete!")
        countDown = False
    if seconds < 0:
        seconds = 59
        minutes -= 1
    if minutes < 0:
        minutes = 59
        hours -= 1
