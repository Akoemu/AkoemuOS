import requests, zipfile, io, os

STORE_URL = "https://tonsite.com/store.json"
GAMES_DIR = "games/"

def fetch_games():
    r = requests.get(STORE_URL)
    return r.json()

def download_game(game):
    print("Téléchargement :", game["name"])

    r = requests.get(game["url"])
    z = zipfile.ZipFile(io.BytesIO(r.content))

    path = os.path.join(GAMES_DIR, game["file"].replace(".zip",""))

    if not os.path.exists(path):
        os.makedirs(path)

    z.extractall(path)

    print("Installé :", game["name"])