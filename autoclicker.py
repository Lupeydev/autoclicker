import keyboard
import time
from pynput.mouse import Button, Controller
import json

mouse = Controller()

with open("clicksettings.json", "r") as file:
    data = json.load(file)

enable_btn = data["enable"]
disable_btn = data["disable"]

click_active = False

while True:
    if keyboard.is_pressed(enable_btn):
        click_active = True
        print("clicker enabled")
        time.sleep(0.15)

    if keyboard.is_pressed(disable_btn):
        click_active = False
        print("clicker disabled")
        time.sleep(0.15)

    if click_active:
        mouse.click(Button.left, 1)
        time.sleep(0.1)