from spotify_screen.screen_controller import SpotifyClient, KeyboardProxy, ScreenController
import mock
import unittest


class TestScreenController:
    def setup(self):
        self.spotify = mock.Mock(SpotifyClient)
        self.keyboard = mock.Mock(KeyboardProxy)
        self.instance = ScreenController(self.spotify, self.keyboard)

    def test_next_should_press_next(self):
        self.instance.next_song()
        self.keyboard.next.assert_called_with()

    def test_play_should_press_play(self):
        self.instance.play_pause()
        self.keyboard.play.assert_called_with()
