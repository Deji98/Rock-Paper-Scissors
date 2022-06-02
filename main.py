# R represent rock
# P represt Paper
# S represent scissors

import random

while True:
    choices = ["R", "P", "S"]

    cpu = random.choice(choices)
    player = None

    while player not in choices:
        print("erorr, please make a choice")
        player = input("R, P, or S?: ").upper()

    if player == cpu:
        print("cpu: ", cpu)
        print("player: ", player)
        print("Tie!")

    elif player == "R":
        if cpu == "P":
            print("cpu: ", cpu)
            print("player: ", player)
            print("You lose!")
        if cpu == "S":
            print("cpu: ", cpu)
            print("player: ", player)
            print("You win!")

    elif player == "S":
        if cpu == "R":
            print("cpu: ", cpu)
            print("player: ", player)
            print("You lose!")
        if cpu == "P":
            print("cpu: ", cpu)
            print("player: ", player)
            print("You win!")

    elif player == "P":
        if cpu == "S":
            print("cpu: ", cpu)
            print("player: ", player)
            print("You lose!")
        if cpu == "R":
            print("cpu: ", cpu)
            print("player: ", player)
            print("You win!")

    play_again = input("Play again? (YES/NO): ").upper()

    if play_again != "YES":
        break

print("Bye!")
