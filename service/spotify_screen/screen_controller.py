from spotify_screen.communicator import SerialCommunicator
from spotify_screen.keyboard_proxy import KeyboardProxy, LinuxKeyboardProxy
from spotify_screen.spotify_client import SpotifyClient
from typing import List, Dict, Union
import json


def bool_to_num(bool):
    return "1" if bool else "0"


class ScreenViewModel:
    def __init__(self, title: str, artists: List[str], album: str, shuffle: bool, repeat: bool, playing: bool):
        self.title = title
        self.artists = artists
        self.album = album
        self.shuffle = shuffle
        self.repeat = repeat
        self.playing = playing

    def to_serial_format(self):
        return u";;".join([self.title, self.artists, self.album, bool_to_num(self.shuffle),bool_to_num(self.repeat),bool_to_num(self.playing)]).encode("utf8")

    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other: 'ScreenViewModel'):
        return self.title == other.title and \
               set(self.artists) == set(other.artists) and \
               self.album == other.album and \
               self.shuffle == other.shuffle and \
               self.repeat == other.repeat and \
               self.playing == other.playing

    def __ne__(self, other):
        return not self.__eq__(other)


class ScreenController:
    def __init__(self, spotify_client: SpotifyClient, serial_com: SerialCommunicator):
        self.serial_com = serial_com
        self._spotify = spotify_client
        self._song_cache = {}  # type: Dict[str,Dict]
        self._current_status = None

    def get_current_viewmodel(self) -> ScreenViewModel:
        status = self._spotify.get_current_status()
        songid = status["track"]["track_resource"]["uri"].split(":")[2]
        track_info = self._song_cache.get(songid, None)
        if track_info is None:
            track_info = self._spotify.get_track_info(songid)
            self._song_cache[songid] = track_info
        return ScreenViewModel(track_info["name"], list(map(lambda artist: artist["name"], track_info["artists"])),
                               track_info["album"]["name"], status["shuffle"], status["repeat"], status["playing"])

    def run(self):
        new_vm = self.get_current_viewmodel()
        if new_vm != self._current_status:
            self._current_status = new_vm
            self.serial_com.send_new_screen(new_vm)
