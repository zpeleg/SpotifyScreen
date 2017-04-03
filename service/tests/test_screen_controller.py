from spotify_screen.screen_controller import SpotifyClient, KeyboardProxy, ScreenController, ScreenViewModel
import mock
from nose.tools import assert_is_not_none, assert_true, assert_equal
import json


class TestScreenController:
    def setup(self):
        self.spotify = mock.Mock(SpotifyClient)  # type: SpotifyClient
        self.keyboard = mock.Mock(KeyboardProxy)  # type: KeyboardProxy
        self.instance = ScreenController(self.spotify, self.keyboard)

    def test_next_should_press_next(self):
        self.instance.next_song()
        self.keyboard.next.assert_called_with()

    def test_play_should_press_play(self):
        self.instance.play_pause()
        self.keyboard.play.assert_called_with()

    def test_get_screen_status_should_return_screen_viewmodel(self):
        self.spotify.get_current_status.return_value = json.loads('{"playing_position": 56.814, "repeat": false, "server_time": 1491256817, "track": {"length": 321, "album_resource": {"location": {"og": "https://open.spotify.com/album/4OpI1vS7xwy4LIJioWDvkn"}, "name": "All We Grow", "uri": "spotify:album:4OpI1vS7xwy4LIJioWDvkn"}, "track_type": "normal", "track_resource": {"location": {"og": "https://open.spotify.com/track/6RbPsqsXQJaqhnwMA971mC"}, "name": "In The Dirt", "uri": "spotify:track:6RbPsqsXQJaqhnwMA971mC"}, "artist_resource": {"location": {"og": "https://open.spotify.com/artist/2LSJrlndCuTpdEluvYHc2E"}, "name": "S. Carey", "uri": "spotify:artist:2LSJrlndCuTpdEluvYHc2E"}}, "play_enabled": true, "prev_enabled": true, "volume": 1, "next_enabled": true, "running": true, "version": 9, "context": {}, "online": true, "shuffle": false, "client_version": "1.0.49.125.g72ee7853", "playing": true, "open_graph_state": {"posting_disabled": true, "private_session": false}}')
        self.spotify.get_track_info.return_value = json.loads('{"album": {"album_type": "album", "href": "https://api.spotify.com/v1/albums/4OpI1vS7xwy4LIJioWDvkn", "name": "All We Grow", "external_urls": {"spotify": "https://open.spotify.com/album/4OpI1vS7xwy4LIJioWDvkn"}, "images": [{"url": "https://i.scdn.co/image/26ae6abfee526ca33e12b47034014aba17265add", "width": 640, "height": 640}, {"url": "https://i.scdn.co/image/ddb5505d1d3fe95fc5f22c17bc93fc4185094b06", "width": 300, "height": 300}, {"url": "https://i.scdn.co/image/f36d71a3108fad1ac30aa621c3a007d57f2aa0f9", "width": 64, "height": 64}], "artists": [{"name": "S. Carey", "external_urls": {"spotify": "https://open.spotify.com/artist/2LSJrlndCuTpdEluvYHc2E"}, "uri": "spotify:artist:2LSJrlndCuTpdEluvYHc2E", "href": "https://api.spotify.com/v1/artists/2LSJrlndCuTpdEluvYHc2E", "type": "artist", "id": "2LSJrlndCuTpdEluvYHc2E"}], "type": "album", "id": "4OpI1vS7xwy4LIJioWDvkn", "available_markets": [], "uri": "spotify:album:4OpI1vS7xwy4LIJioWDvkn"}, "popularity": 2, "name": "In The Dirt", "external_urls": {"spotify": "https://open.spotify.com/track/6RbPsqsXQJaqhnwMA971mC"}, "preview_url": null, "explicit": false, "uri": "spotify:track:6RbPsqsXQJaqhnwMA971mC", "track_number": 3, "disc_number": 1, "href": "https://api.spotify.com/v1/tracks/6RbPsqsXQJaqhnwMA971mC", "artists": [{"name": "S. Carey", "external_urls": {"spotify": "https://open.spotify.com/artist/2LSJrlndCuTpdEluvYHc2E"}, "uri": "spotify:artist:2LSJrlndCuTpdEluvYHc2E", "href": "https://api.spotify.com/v1/artists/2LSJrlndCuTpdEluvYHc2E", "type": "artist", "id": "2LSJrlndCuTpdEluvYHc2E"}], "duration_ms": 321813, "external_ids": {"isrc": "US38Y1018103"}, "type": "track", "id": "6RbPsqsXQJaqhnwMA971mC", "available_markets": []}')
        viewmodel = self.instance.get_current_viewmodel()  # type: ScreenViewModel
        assert_equal(viewmodel.title, "In The Dirt")
        assert_equal(viewmodel.album, "All We Grow")
        assert_equal(viewmodel.artists, ["S. Carey"])
        assert_equal(viewmodel.shuffle, False)
        assert_equal(viewmodel.repeat, False)
        assert_equal(viewmodel.playing, True)

    def test_get_screen_status_when_multi_artists_should_return_screen_viewmodel(self):
        self.spotify.get_current_status.return_value = json.loads('{"playing_position": 22.313, "repeat": false, "shuffle": true, "play_enabled": true, "playing": true, "volume": 1, "next_enabled": true, "running": true, "version": 9, "track": {"album_resource": {"uri": "spotify:album:3kVdysNnlL5oTzhMERRLLo", "name": "Absolute Greatest", "location": {"og": "https://open.spotify.com/album/3kVdysNnlL5oTzhMERRLLo"}}, "track_type": "normal", "length": 248, "track_resource": {"uri": "spotify:track:3Eh33UmqyS7PGIfaNQgr0d", "name": "Under Pressure", "location": {"og": "https://open.spotify.com/track/3Eh33UmqyS7PGIfaNQgr0d"}}, "artist_resource": {"uri": "spotify:artist:1dfeR4HaWDbWqFHLkxsg1d", "name": "Queen", "location": {"og": "https://open.spotify.com/artist/1dfeR4HaWDbWqFHLkxsg1d"}}}, "context": {}, "online": true, "server_time": 1491256948, "client_version": "1.0.49.125.g72ee7853", "prev_enabled": false, "open_graph_state": {"posting_disabled": true, "private_session": false}}')
        self.spotify.get_track_info.return_value = json.loads('{"album": {"album_type": "compilation", "href": "https://api.spotify.com/v1/albums/3kVdysNnlL5oTzhMERRLLo", "name": "Absolute Greatest", "artists": [{"name": "Queen", "external_urls": {"spotify": "https://open.spotify.com/artist/1dfeR4HaWDbWqFHLkxsg1d"}, "uri": "spotify:artist:1dfeR4HaWDbWqFHLkxsg1d", "href": "https://api.spotify.com/v1/artists/1dfeR4HaWDbWqFHLkxsg1d", "type": "artist", "id": "1dfeR4HaWDbWqFHLkxsg1d"}], "images": [{"url": "https://i.scdn.co/image/ba49ea8bb2bacfbbb7b8b2c87d183a096fc191b8", "width": 640, "height": 640}, {"url": "https://i.scdn.co/image/85063eaa0fa521bb1bec29a14875a3efb21f5f79", "width": 300, "height": 300}, {"url": "https://i.scdn.co/image/35625172a782e43d237d6cf9b1089a0d49047fff", "width": 64, "height": 64}], "external_urls": {"spotify": "https://open.spotify.com/album/3kVdysNnlL5oTzhMERRLLo"}, "type": "album", "id": "3kVdysNnlL5oTzhMERRLLo", "available_markets": ["DO", "GT", "HN", "NI", "PA", "SV"], "uri": "spotify:album:3kVdysNnlL5oTzhMERRLLo"}, "popularity": 14, "name": "Under Pressure", "external_urls": {"spotify": "https://open.spotify.com/track/3Eh33UmqyS7PGIfaNQgr0d"}, "preview_url": "https://p.scdn.co/mp3-preview/faa901c4330fe2bbeb984e4c54acccabeff29370?cid=null", "explicit": false, "uri": "spotify:track:3Eh33UmqyS7PGIfaNQgr0d", "track_number": 8, "disc_number": 1, "href": "https://api.spotify.com/v1/tracks/3Eh33UmqyS7PGIfaNQgr0d", "artists": [{"name": "Queen", "external_urls": {"spotify": "https://open.spotify.com/artist/1dfeR4HaWDbWqFHLkxsg1d"}, "uri": "spotify:artist:1dfeR4HaWDbWqFHLkxsg1d", "href": "https://api.spotify.com/v1/artists/1dfeR4HaWDbWqFHLkxsg1d", "type": "artist", "id": "1dfeR4HaWDbWqFHLkxsg1d"}, {"name": "David Bowie", "external_urls": {"spotify": "https://open.spotify.com/artist/0oSGxfWSnnOXhD2fKuz2Gy"}, "uri": "spotify:artist:0oSGxfWSnnOXhD2fKuz2Gy", "href": "https://api.spotify.com/v1/artists/0oSGxfWSnnOXhD2fKuz2Gy", "type": "artist", "id": "0oSGxfWSnnOXhD2fKuz2Gy"}], "duration_ms": 243426, "external_ids": {"isrc": "GBCEG9400046"}, "type": "track", "id": "3Eh33UmqyS7PGIfaNQgr0d", "available_markets": ["DO", "GT", "HN", "NI", "PA", "SV"]}')
        viewmodel = self.instance.get_current_viewmodel()  # type: ScreenViewModel
        assert_equal(viewmodel.title, "Under Pressure")
        assert_equal(viewmodel.album, "Absolute Greatest")
        assert_equal(viewmodel.artists, ["Queen", "David Bowie"])
        assert_equal(viewmodel.shuffle, True)
        assert_equal(viewmodel.repeat, False)
        assert_equal(viewmodel.playing, True)
