import requests
import urllib.parse
from requests.exceptions import ConnectionError, ReadTimeout


class AuthenticationTokens:
    def __init__(self, oauth: str, csrf: str, address: str):
        self.oauth = oauth
        self.csrf = csrf
        self.address = address

    def __repr__(self):
        return "oauth={}\ncsrf={}\naddress={}".format(self.oauth, self.csrf, self.address)


class SpotifyAuthenticator:
    def authenticate(self):
        oauth = self.__get_oauth()
        address = self.__get_address()
        csrf = self.__get_csrf(address)
        return AuthenticationTokens(oauth, csrf, address)

    def __get_oauth(self):
        response = requests.get("https://open.spotify.com/token")
        return response.json()["t"]

    def __get_address(self):
        for port in range(4370, 4390):
            try:
                address = "http://screen.spotilocal.com:" + str(port)
                requests.get(address, timeout=0.01)
                return address
            except ConnectionError:
                pass
            except ReadTimeout:
                pass
        raise Exception("Could not find spotilocal address")

    def __get_csrf(self, spotilocal_address):
        url = urllib.parse.urljoin(spotilocal_address, "/simplecsrf/token.json")
        response = requests.get(url, headers={'Origin': 'https://open.spotify.com'})
        return response.json()["token"]
