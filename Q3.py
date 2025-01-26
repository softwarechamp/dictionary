# Create a dictionary with player names as keys and default their scores to 0
n = int(input("Enter the number of players in the match: "))
players = {input(f"Enter the name of player {i + 1}: "): 0 for i in range(n)}

# Display all player names
# print("\nPlayers in this match:", ', '.join(players.keys()))
# print(f"Players i this match are: \n",players.keys())
print(f"Players in this match are: \n" )
for p in players:
    print(p,end="\t")

# Update scores for each player
for player in players:
    score = int(input(f"\nEnter the score for {player}: "))
    players[player] = score

player_name=input("Enter player name to see details: ")
print(f"Player Name: {player_name}\t Runs Scored: {players[player_name]}")

total_score = 0
for score in players.values():
    total_score += score
print(f"Total score of all players: {total_score}")

max_scorer = max(players, key=players.get)
min_scorer = min(players, key=players.get)
print(f"Maximum scorer: {max_scorer} with {players[max_scorer]} runs")
print(f"Minimum scorer: {min_scorer} with {players[min_scorer]} runs")
