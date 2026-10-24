teams = ["CSK", "MI", "RCB", "KKR", "GT"]
points = [12, 8, 15, 10, 14]

result = dict(zip(teams, points))

for team, point in result.items():
    if point > 10:
        print(team, point)