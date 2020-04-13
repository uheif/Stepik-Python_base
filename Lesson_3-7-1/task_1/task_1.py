def get_scores(goals1, goals2):
    team1_scores = 3 if goals1 > goals2 else 0 if goals1 < goals2 else 1
    team2_scores = 3 if goals2 > goals1 else 0 if goals2 < goals1 else 1
    return team1_scores, team2_scores


def table(scores):
    was_game = 1
    win = 1 if scores == 3 else 0
    draw = 1 if scores == 1 else 0
    lose = 1 if scores == 0 else 0
    return [was_game, win, draw, lose, scores]


plays: int = int(input())
pivot_table: dict = {}
for i in range(plays):
    team1, goals1, team2, goals2 = input().split(';')
    teams: tuple = (team1, team2)
    scores: tuple = get_scores(int(goals1), int(goals2))
    for j in range(len(teams)):
        team_table: list = table(scores[j])
        if teams[j] not in pivot_table:
            pivot_table[teams[j]] = team_table
        else:
            old_table: list = pivot_table[teams[j]]
            pivot_table[teams[j]] = list(map(lambda a, b: a + b, team_table, old_table))

for team, table in pivot_table.items():
    print(team + ':', *table)
