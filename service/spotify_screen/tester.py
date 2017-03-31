from spotify_screen.spotify_authenticator import SpotifyAuthenticator
from spotify_screen.spotify_client import SpotifyClient


def main():
    client = SpotifyClient(SpotifyAuthenticator())
    client.connect()
    print(client.get_current_status())
    print(client.get_track_info("6ieE8e0EZgi5lNYeQtzh8H"))

if __name__ == '__main__':
    main()