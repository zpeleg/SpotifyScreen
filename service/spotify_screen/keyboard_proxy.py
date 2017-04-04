import pyautogui
import subprocess


# https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys
class KeyboardProxy:
    def play(self):
        pyautogui.press("playpause")

    def next(self):
        pyautogui.press("nexttrack")


class LinuxKeyboardProxy:
    def __init__(self):
        pass

    def init(self):
        try:
            subprocess.call("xdotool")
        except FileNotFoundError:
            raise Exception("xdotool is not installed. Get it from apt-get.")

    def play(self):
        subprocess.call(["xdotool", "key", "XF86AudioPlay"])

    def next(self):
        subprocess.call(["xdotool", "key", "XF86AudioNext"])
