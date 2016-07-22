import csv
from Player import Player

BASE_PATH = "text/"

def get_all_players(file_path):
    file_path = BASE_PATH + file_path
    players = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == "Position":
                continue
            else:
                players.append(Player(row[1], row[5], row[0], row[2], row[4]))
    return players