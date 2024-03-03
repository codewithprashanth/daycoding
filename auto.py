import pyautogui
import time
import keyboard

def main():
    # Open Notepad
    pyautogui.press('winleft')
    pyautogui.typewrite('notepad\n')
    time.sleep(1)  # Wait for Notepad to open

    # Type space repeatedly until the 'Esc' key is pressed
    while True:
        pyautogui.press('space')
        if keyboard.is_pressed('esc'):
            break

if __name__ == "__main__":
    main()
