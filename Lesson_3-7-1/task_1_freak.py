data = [input().split(';') for i in range(int(input()))]
teams = {team: [] for team in set(data[i][j] for i in range(len(data)) for j in range(0, 3, 2))}

for game in data:
    names = game[0], game[2]
    goals = int(game[1]), int(game[3])
    for i in range(2):
        teams[names[i]].append(3 if goals[i] > goals[i - 1] else 1 if game[i] == game[i - 1] else 0)

for team in teams:
    print(f"{team}: {len(teams[team])} {teams[team].count(3)} {teams[team].count(1)} "
          f"{teams[team].count(0)} {sum(teams[team])}")