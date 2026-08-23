import random
def roll():
    roll = random.randint(1,6)
    return roll
while True:
    players = input("Enter the number of players (2-4) : ")
    if players.isdigit():
        players = int(players)
        if 2<= players <5 :
            break
        else:
            print("Error! Must be between 2 - 4 players")
    else:
        print("Invalid choice, try again")
max_scores = 50
player_scores = [0 for _ in range(players)]

while max(player_scores)< max_scores:
    for player_index in range(players):
        print("\nPlayer number", player_index+1,"turn has just started!")
        print("Your total score is: ",player_scores[player_index],"\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? [Press q to quit] ")
            if should_roll.lower() == "q":
                quit()
            if should_roll.lower() !="y":
                break
            value = roll()
            if value == 1:
                print("You rolled 1! Turn finished")
                current_score = 0
                break
            else:
                print("You rolled a: ",value)
                current_score += value
            print("Your current score is: ",current_score)
        player_scores[player_index] += current_score
        print("Your total score is: ",player_scores[player_index])
        if player_scores[player_index] >= max_scores:
            break
max_scores = max(player_scores)
winning_index = player_scores.index(max_scores)
print("Player number",winning_index+1,"is the winner with a score of", max_scores)