import random

R = "Rock"
P = "Paper"
S = "Scissors"

moves = [R, P, S]

while True:
    computer = random.choice(moves).upper()
    player = input(" Rock ,Paper or, Scissors:  ").upper()
    print("CPU", "(", (computer), ")", ",", "Player", "(", (player), ")")

    if player == computer:
        print("There is a tie")
    elif player == R.upper():
        if computer == S.upper():
            print("player", "wins")
        else:
            print("CPU", "wins")
    elif player == P.upper():
        if computer == R.upper():
            print("player", "wins")
        else:
            print("CPU", "wins")
    elif player == S.upper():
        if computer == P.upper():
            print("player", "wins")
        else:
            print("CPU", "wins")
    else:
        print("Wrong entry!!!")

