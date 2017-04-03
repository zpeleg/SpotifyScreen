from spotify_screen.spotify_authenticator import SpotifyAuthenticator
from requests.exceptions import ConnectionError
import mock
from nose.tools import assert_equal
from nose.tools import assert_regexp_matches
import re


class MockResponse:
    def __init__(self, json):
        self._json = json

    def json(self):
        return self._json


@mock.patch("spotify_screen.spotify_authenticator.requests")
class TestSpotifyAuthenticator:
    def setup(self):
        self.mixedresponse = {"t": "oauthtoken",
                              "token": "csrftoken"}
        self.instance = SpotifyAuthenticator()

    def test_authenticate_should_return_oauth_token(self, mock_requests):
        mock_requests.get.return_value = MockResponse(self.mixedresponse)
        tokens = self.instance.authenticate()
        assert_equal(tokens.oauth, "oauthtoken")
        mock_requests.get.assert_any_call("https://open.spotify.com/token")

    def test_authenticate_should_return_spotilocal_address(self, mock_requests):
        regex = r"http://\w+\.spotilocal\.com:(\d+)/?"

        def get(address, headers=None):
            match = re.match(regex, address)
            if not match or match.groups()[0] == '4380':
                return mock.DEFAULT
            else:
                raise ConnectionError()

        mock_requests.get.side_effect = get
        tokens = self.instance.authenticate()
        assert_regexp_matches(tokens.address, r"http://\w+\.spotilocal\.com:4380/?")

    @mock.patch.object(SpotifyAuthenticator, '_SpotifyAuthenticator__get_address',
                       return_value="https://screen.spotilocal.com:4380")
    def test_authenticate_should_return_csrf_token(self, method, mock_requests):
        mock_requests.get.return_value = MockResponse(self.mixedresponse)
        tokens = self.instance.authenticate()
        assert_equal(tokens.csrf, "csrftoken")
        mock_requests.get.assert_any_call("https://screen.spotilocal.com:4380/simplecsrf/token.json", headers={'Origin': 'https://open.spotify.com'})
