from spotify_screen.keyboard_proxy import KeyboardProxy, LinuxKeyboardProxy
from spotify_screen.screen_controller import ScreenController
from spotify_screen.spotify_authenticator import SpotifyAuthenticator
from spotify_screen.spotify_client import SpotifyClient
import time


def main():
    client = SpotifyClient(SpotifyAuthenticator())
    client.connect()
    keyboard = LinuxKeyboardProxy()
    controller = ScreenController(client, keyboard)
    print(controller.get_current_viewmodel())
    controller.play_pause()
    time.sleep(2)
    print(controller.get_current_viewmodel())
    controller.play_pause()


if __name__ == '__main__':
    main()
