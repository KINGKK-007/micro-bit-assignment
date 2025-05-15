from microbit import display, accelerometer, button_a, button_b, uart, running_time, sleep, Image

# Initialize UART over USB
uart.init(baudrate=115200)

# State for double-press detection
last_a_time = 0
a_count     = 0
last_b_time = 0
b_count     = 0
DOUBLE_WINDOW = 2000  # ms

while True:
    now = running_time()

    # Shake → Play/Pause
    if accelerometer.was_gesture('shake'):
        uart.write('SP\n')
        display.show(Image.MUSIC_QUAVER)    # ← replaced PLAY with MUSIC_QUAVER
        sleep(500)
        display.clear()

    # Button A logic: single → PREV, double → vol down
    if button_a.was_pressed():
        if a_count == 1 and now - last_a_time <= DOUBLE_WINDOW:
            uart.write('VD\n')
            display.show('-')
            sleep(500)
            display.clear()
            a_count = 0
        else:
            a_count     = 1
            last_a_time = now

    # Button B logic: single → NEXT, double → vol up
    if button_b.was_pressed():
        if b_count == 1 and now - last_b_time <= DOUBLE_WINDOW:
            uart.write('VU\n')
            display.show('+')
            sleep(500)
            display.clear()
            b_count = 0
        else:
            b_count     = 1
            last_b_time = now

    # After window expires, treat a lone A as PREV
    if a_count == 1 and now - last_a_time > DOUBLE_WINDOW:
        uart.write('PREV\n')
        display.show(Image.ARROW_W)
        sleep(500)
        display.clear()
        a_count = 0

    # After window expires, treat a lone B as NEXT
    if b_count == 1 and now - last_b_time > DOUBLE_WINDOW:
        uart.write('NEXT\n')
        display.show(Image.ARROW_E)
        sleep(500)
        display.clear()
        b_count = 0

    sleep(100)