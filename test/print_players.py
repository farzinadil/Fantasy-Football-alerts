import json
with open("public/players.json") as players:
    players = json.load(players)
    for player in players["players"]:
        print(player)
