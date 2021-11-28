import json

players = {"players": []}

with open('public/data.json') as json_file:
    data = json.load(json_file)

    # Get the top 500 players from the data
    i = 0
    while i < 500:
        i += 1
        players["players"].append(data['players'][i]['player_name'])

# Write the top 500 players to a json file
with open('public/players.json', 'w') as output:
    json.dump(players, output)
