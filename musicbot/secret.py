import configparser
import os


def set_secrets(config_file):
    config = configparser.ConfigParser(interpolation=None)
    config.read(config_file, encoding="utf-8")
    config.set(
        "Credentials", "Token", os.getenv("TOKEN")
    )
    config.set(
        "Credentials", "Spotify_ClientID", os.getenv("SPOTIFY_CLIENTID")
    )
    config.set(
        "Credentials", "Spotify_ClientSecret", os.getenv("SPOTIFY_CLIENTSECRET")
    )
    return config
