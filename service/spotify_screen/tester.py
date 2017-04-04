from spotify_screen.keyboard_proxy import KeyboardProxy
from spotify_screen.screen_controller import ScreenController
from spotify_screen.spotify_authenticator import SpotifyAuthenticator
from spotify_screen.spotify_client import SpotifyClient
import time


# TODO: Change KeyboardProxy to use xdotool key XF86AudioPlay on linux, and whatever on windows

def main():
    client = SpotifyClient(SpotifyAuthenticator())
    client.connect()
    keyboard = KeyboardProxy()
    controller = ScreenController(client, keyboard)
    print(controller.get_current_viewmodel())
    controller.play_pause()
    time.sleep(0.4)
    print(controller.get_current_viewmodel())
    controller.play_pause()


if __name__ == '__main__':
    main()
