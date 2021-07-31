import random

player_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    player_pick = input("Type R or Rock, P or Paper, S or Scissors or Q to quit: ").lower()
    if player_pick == "q":
        break

    if player_pick not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if (player_pick == "rock" or player_pick == "r") and computer_pick == "scissors":
        print("You won!")
        player_wins += 1

    elif (player_pick == "paper" or player_pick == "p") and computer_pick == "paper":
        print("You won!")
        player_wins += 1

    elif (player_pick == "scissors" or player_pick == "s") and computer_pick == "paper":
        print("You won!")
        player_wins += 1

    elif player_pick == computer_pick:
        print("It's a draw! Try again")
        player_wins += 0

    else:
        print("You lost!")
        computer_wins += 1

print("You won", player_wins, "times.")
print("The computer won", computer_wins, "times.")
print("See you next time!")
