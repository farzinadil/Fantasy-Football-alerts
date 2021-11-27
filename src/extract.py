import json

players = {"players": []}

with open('public/data.json') as json_file:
    data = json.load(json_file)

    i = 0
    while i < 500:
        i += 1
        players["players"].append(data['players'][i]['player_name'])


with open('public/players.json', 'w') as output:
    json.dump(players, output)
