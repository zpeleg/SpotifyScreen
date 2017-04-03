from nose.tools import assert_equal
import mock
from spotify_screen.keyboard_proxy import KeyboardProxy


@mock.patch("spotify_screen.keyboard_proxy.pyautogui")
class TestKeyboardProxy:
    def setup(self):
        self.instance = KeyboardProxy()

    def test_play_should_simulate_play_key_press(self, mock_pyautogui):
        self.instance.play()
        mock_pyautogui.press.assert_called_with("playpause")

    def test_next_should_simulate_nexttrack_key_press(self, mock_pyautogui):
        self.instance.next()
        mock_pyautogui.press.assert_called_with("nexttrack")
