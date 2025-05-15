import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# ==== Configuration ====
JIO_SAAVN_URL       = "https://www.jiosaavn.com/"
PLAYER_CONTROLS     = "#player > div.c-player__panel > ul.c-player__controls.u-margin-bottom-none\\@sm"
PLAY_PAUSE_BTN      = PLAYER_CONTROLS + " > li:nth-child(3)"
NEXT_BTN            = PLAYER_CONTROLS + " > li.c-player__btn.c-player__btn-next"
PREV_BTN            = PLAYER_CONTROLS + " > li.c-player__btn.c-player__btn-prev"

# ==== Helper functions ====
def init_driver():
    driver = webdriver.Chrome()  # make sure chromedriver is in PATH
    driver.get(JIO_SAAVN_URL)
    time.sleep(5)  # wait for the player to load
    return driver

def click_button(driver, selector):
    try:
        btn = driver.find_element(By.CSS_SELECTOR, selector)
        btn.click()
    except Exception as e:
        print(f"[!] Could not click {selector}: {e}")

def get_mute_button(driver):
    for sel in ('button[aria-label="Mute"]', 'button[title="Mute"]'):
        try:
            return driver.find_element(By.CSS_SELECTOR, sel)
        except:
            pass
    return None

def click_mute(driver):
    btn = get_mute_button(driver)
    if btn:
        btn.click()
    else:
        print("[!] Mute button not found.")

def change_volume(driver, delta: float):
    """
    Change volume by delta (±0.0–1.0). Positive raises, negative lowers.
    """
    try:
        # adjust audio.volume and clamp between 0 and 1
        driver.execute_script("""
            let a = document.querySelector('audio');
            if (a) {
                let v = Math.min(1, Math.max(0, a.volume + arguments[0]));
                a.volume = v;
                a.dispatchEvent(new Event('volumechange'));
                return v;
            }
            return null;
        """, delta)
    except Exception as e:
        print(f"[!] Could not change volume: {e}")

# ==== Main interactive loop ====
def main():
    driver = init_driver()
    try:
        while True:
            print("""
Choose an action:
  1. Play/Pause
  2. Next Track
  3. Previous Track
  4. Quit
  5. Mute/Unmute
  6. Volume Up
  7. Volume Down
""")
            choice = input("Enter 1-7: ").strip()
            if choice == "1":
                click_button(driver, PLAY_PAUSE_BTN)
            elif choice == "2":
                click_button(driver, NEXT_BTN)
            elif choice == "3":
                click_button(driver, PREV_BTN)
            elif choice == "4":
                print("Exiting…")
                break
            elif choice == "5":
                click_mute(driver)
            elif choice == "6":
                change_volume(driver, 0.1)
            elif choice == "7":

                change_volume(driver, -0.1)
            else:
                print("Invalid choice. Please enter a number from 1 to 7.")
            time.sleep(0.2)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
