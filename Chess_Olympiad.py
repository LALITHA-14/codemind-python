# cook your dish here
x, y, z = map(int, input().split())

# Calculate points of the team
current_points = x + (y * 0.5)

# Remaining games
remaining_games = 4 - (x + y + z)

# Maximum possible points your team can obtain
max_possible_points = current_points + remaining_games

# Opponent's maximum points (assuming they won all their games)
opponent_points = (z + (y * 0.5))

if max_possible_points > opponent_points:
    print("Yes")
else:
    print("No")
