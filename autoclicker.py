import keyboard
import time
from pynput.mouse import Button, Controller

mouse = Controller()

click_active = False

while True:
    if keyboard.is_pressed("q"):
        click_active = True
        print("clicker enabled")
        time.sleep(0.15)

    if keyboard.is_pressed("e"):
        click_active = False
        print("clicker disabled")
        time.sleep(0.15)

    if click_active:
        mouse.click(Button.left, 1)
        time.sleep(0.1)