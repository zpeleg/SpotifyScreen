from spotify_screen.spotify_authenticator import SpotifyAuthenticator

def main():
    auth = SpotifyAuthenticator()
    tokens = auth.authenticate()
    print(tokens)
    pass

if __name__ == '__main__':
    main()