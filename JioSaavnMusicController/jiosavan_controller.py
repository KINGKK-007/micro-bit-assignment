import time
import serial
from jiosavan import init_driver, click_button, change_volume, PLAY_PAUSE_BTN, NEXT_BTN, PREV_BTN

# === Adjust this to your Micro:bit’s COM port ===
SERIAL_PORT = 'COM9'       # e.g. 'COM3' on Windows or '/dev/ttyACM0' on Linux/macOS
BAUD_RATE    = 115200

def main():
    # Open serial to Micro:bit
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

    # Start the JioSaavn browser session
    driver = init_driver()  # :contentReference[oaicite:0]{index=0}&#8203;:contentReference[oaicite:1]{index=1}

    try:
        while True:
            if ser.in_waiting:
                line = ser.readline().decode('utf-8').strip()
                if not line:
                    continue

                if line == 'SP':
                    click_button(driver, PLAY_PAUSE_BTN)    # Play/Pause :contentReference[oaicite:2]{index=2}&#8203;:contentReference[oaicite:3]{index=3}
                elif line == 'PREV':
                    click_button(driver, PREV_BTN)          # Previous :contentReference[oaicite:4]{index=4}&#8203;:contentReference[oaicite:5]{index=5}
                elif line == 'NEXT':
                    click_button(driver, NEXT_BTN)          # Next :contentReference[oaicite:6]{index=6}&#8203;:contentReference[oaicite:7]{index=7}
                elif line == 'VU':
                    change_volume(driver, 0.1)              # Vol Up :contentReference[oaicite:8]{index=8}&#8203;:contentReference[oaicite:9]{index=9}
                elif line == 'VD':
                    change_volume(driver, -0.1)             # Vol Down :contentReference[oaicite:10]{index=10}&#8203;:contentReference[oaicite:11]{index=11}

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Exiting…")
    finally:
        driver.quit()
        ser.close()

if __name__ == '__main__':
    main()
