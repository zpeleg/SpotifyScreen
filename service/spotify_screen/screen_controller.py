from spotify_screen.keyboard_proxy import KeyboardProxy
from spotify_screen.spotify_client import SpotifyClient


class ScreenController:
    def __init__(self, spotify_client, keyboard_proxy):
        self._spotify = spotify_client
        self._keyboard = keyboard_proxy

    def next_song(self):
        self._keyboard.next()

    def play_pause(self):
        self._keyboard.play()
