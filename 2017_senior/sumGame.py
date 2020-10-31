N = int(input())
team1 = str(input())
team2 = str(input())

team1_scores = team1.split(" ")
team2_scores = team2.split(" ")

team1_sum = 0
team2_sum = 0
index = 0

for i in range(N):
    team1_sum += int(team1_scores[i])
    team2_sum += int(team2_scores[i])
    if team1_sum == team2_sum:
        index = i + 1

print(index)