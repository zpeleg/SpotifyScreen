import requests
import time
import urllib.parse


class SpotifyClient:
    def __init__(self, authenticator):
        self.__authenticator = authenticator
        self.__tokens = None

    def connect(self):
        self.__tokens = self.__authenticator.authenticate()

    def get_track_info(self, trackid):
        return requests.get('https://api.spotify.com/v1/tracks/' + trackid).json()

    def get_current_status(self):
        url = urllib.parse.urljoin(self.__tokens.address, '/remote/status.json')
        return requests.get(url, params={
            "oauth": self.__tokens.oauth,
            "csrf": self.__tokens.csrf,
            "ref": "",
            "cors": "",
            "_": int(time.time())
        }).json()
