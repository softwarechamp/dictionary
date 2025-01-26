# Create a dictionary with player names as keys and default their scores to 0
n = int(input("Enter the number of players in the match: "))
players = {input(f"Enter the name of player {i + 1}: "): 0 for i in range(n)}

# Display all player names
print("\nPlayers in this match:", ', '.join(players.keys()))

# Update scores for each player
for player in players:
    score = int(input(f"Enter the score for {player}: "))
    players[player] = score

# Menu-driven options
while True:
    print("\nMenu:")
    print("1. Display runs scored by a player")
    print("2. Calculate and display the total score of all players")
    print("3. Display the player with the maximum and minimum scores")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        # Display runs scored by a player
        name = input("Enter the player's name: ")
        if name in players:
            print(f"Player: {name}, Score: {players[name]}")
        else:
            print("Player not found.")
    
    elif choice == 2:
        # Calculate and display the total score
        total_score = 0
        for score in players.values():
            total_score += score
        print(f"Total score of all players: {total_score}")
    
    elif choice == 3:
        # Find maximum and minimum scorer
        max_scorer = max(players, key=players.get)
        min_scorer = min(players, key=players.get)
        print(f"Maximum scorer: {max_scorer} with {players[max_scorer]} runs")
        print(f"Minimum scorer: {min_scorer} with {players[min_scorer]} runs")
    
    elif choice == 4:
        # Exit the program
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
