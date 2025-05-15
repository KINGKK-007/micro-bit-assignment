from microbit import compass, display, accelerometer
from microbit import sleep

display.scroll("Shake!")
while not accelerometer.was_gesture('shake'):
    sleep(100)

compass.calibrate()

while True:
    h = compass.heading()  # 0–360°
    if h < 45 or h >= 315:
        display.show("N")
    elif h < 135:
        display.show("E")
    elif h < 225:
        display.show("S")
    else:
        display.show("W")
    sleep(300)