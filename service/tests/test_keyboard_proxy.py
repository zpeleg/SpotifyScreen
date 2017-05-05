import mock
from spotify_screen.keyboard_proxy import KeyboardProxy, LinuxKeyboardProxy
from nose.tools import assert_raises, assert_regexp_matches, assert_true


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


@mock.patch("spotify_screen.keyboard_proxy.subprocess")
class TestLinuxKeyboardProxy:
    def setup(self):
        self.instance = LinuxKeyboardProxy()

    def test_init_when_xdotool_isnt_installed_should_raise_exception(self, subprocess):
        # Arrange
        def call_side_effect(args):
            if "xdotool" in args:
                raise FileNotFoundError()
            return mock.DEFAULT

        subprocess.call.side_effect = call_side_effect
        # Act
        with assert_raises(Exception) as exceptionassert:
            self.instance.init()
        # Assert
        ex = exceptionassert.exception
        # Make sure that the exception sort of makes sense
        assert_true(ex.args, "There must be a message")
        assert_regexp_matches(ex.args[0], "xdotool")
        assert_regexp_matches(ex.args[0], "not installed")

    def test_pause_play(self, subprocess):
        self.instance.play()
        subprocess.call.assert_called_once_with(["xdotool", "key", "XF86AudioPlay"])

    def test_next(self,subprocess):
        self.instance.next()
        subprocess.call.assert_called_once_with(["xdotool", "key", "XF86AudioNext"])

