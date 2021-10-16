import configparser
import os


def set_config(config_file):
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


def set_permissions(permissions_file):
    permissions = configparser.ConfigParser(interpolation=None)
    permissions.read(permissions_file, encoding="utf-8")
    permissions.set(
        "DJ", "GrantToRoles", os.getenv("DJ_GrantToRoles")
    )
    return permissions
