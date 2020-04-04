"""
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на
стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение 0, за ничью 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
"""
class Team:
    teams: dict = {}
    games = wins = draws = loses = score = goals = 0

    def __init__(self, name):
        self.name: str = name

    def play_game(self, other):
        self.games += 1
        self.wins += int(self.goals > other.goals)
        self.draws += int(self.goals == other.goals)
        self.loses += int(self.goals < other.goals)
        self.score = self.wins * 3 + self.draws


class GameEvent:

    def __init__(self, names_goals: list):
        self.names = names_goals[0], names_goals[2]
        self.result = int(names_goals[1]), int(names_goals[3])
        for team_name, goals in zip(self.names, self.result):
            if team_name not in Team.teams:
                Team.teams[team_name] = Team(team_name)
            Team.teams[team_name].goals = goals


for i in range(int(input())):
    this_game = GameEvent(input().split(';'))
    for j in range(0, -2, -1):
        Team.teams[this_game.names[j]].play_game(Team.teams[this_game.names[j + 1]])

for team in Team.teams.values():
    print(f"{team.name}: {team.games} {team.wins} {team.draws} {team.loses} {team.score}")
