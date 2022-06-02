import random

while True:
    choices = ["R", "P", "S"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("R, P, or S?: ").upper()

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!")

    elif player == "R":
        if computer == "P":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "S":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "S":
        if computer == "R":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "P":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "P":
        if computer == "S":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "R":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    play_again = input("Play again? (YES/NO): ").upper()

    if play_again != "YES":
        break

print("Bye!")
