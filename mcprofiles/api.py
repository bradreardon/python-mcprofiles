import requests
from json import JSONEncoder

def to_uuid(users):
    """
    Provides easy method for checking UUID of one or multiple users.
    Will always return a dictionary with the keys representing usernames.

    If a username is invalid, it will not be included in the response dictionary.

    :param users: String or list of usernames to convert to UUIDs.
    :return: A dictionary mapping all (valid) users to UUIDs.
    """
    resp = {}

    r = requests.post(
        "https://api.mojang.com/profiles/minecraft",
        headers={"Content-Type": "application/json"},
        data=JSONEncoder().encode(users)
    )

    for pair in r.json():
        resp[pair['name']] = pair['id']

    return resp