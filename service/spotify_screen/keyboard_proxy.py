import pyautogui

# https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys
class KeyboardProxy:
    def play(self):
        pyautogui.press("playpause")

    def next(self):
        pyautogui.press("nexttrack")
