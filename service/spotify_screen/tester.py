from spotify_screen.communicator import SerialCommunicator
from spotify_screen.keyboard_proxy import KeyboardProxy, LinuxKeyboardProxy
from spotify_screen.screen_controller import ScreenController
from spotify_screen.spotify_authenticator import SpotifyAuthenticator
from spotify_screen.spotify_client import SpotifyClient
from time import sleep


def main():
    client = SpotifyClient(SpotifyAuthenticator())
    client.connect()
    keyboard = LinuxKeyboardProxy()
    serial = SerialCommunicator(keyboard)
    controller = ScreenController(client, serial)
    serial.connect()
    while 1:
        serial.listen()
        controller.check_changes()
        sleep(0.1)



if __name__ == '__main__':
    main()
