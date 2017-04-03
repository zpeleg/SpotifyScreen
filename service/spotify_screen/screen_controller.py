from spotify_screen.keyboard_proxy import KeyboardProxy
from spotify_screen.spotify_client import SpotifyClient
from typing import List


class ScreenViewModel:
    def __init__(self, title: str, artists: List[str], album: str, shuffle: bool, repeat: bool, playing: bool):
        self.title = title
        self.artists = artists
        self.album = album
        self.shuffle = shuffle
        self.repeat = repeat
        self.playing = playing


class ScreenController:
    def __init__(self, spotify_client: SpotifyClient, keyboard_proxy: KeyboardProxy):
        self._spotify = spotify_client
        self._keyboard = keyboard_proxy

    def next_song(self):
        self._keyboard.next()

    def play_pause(self):
        self._keyboard.play()

    def get_current_viewmodel(self):
        status = self._spotify.get_current_status()
        songid = status["track"]["track_resource"]["uri"].split(":")[2]
        track_info = self._spotify.get_track_info(songid)
        return ScreenViewModel(track_info["name"], list(map(lambda artist: artist["name"], track_info["artists"])),
                               track_info["album"]["name"], status["shuffle"], status["repeat"], status["playing"])
