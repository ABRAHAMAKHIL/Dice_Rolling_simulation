import random
from time import *
def main():
    Player1 = 0
    Player2 = 0
    Player1wins = 0
    Player2wins = 0
    rounds = 1
    while rounds != 4:
        print("Round = " + str(rounds))
        Player1 = roll()
        Player2 = roll()

        print("Player 1 rolls:" + str(Player1))
        print("Player 2 rolls:" + str(Player2))
        if Player1 == Player2:
            print("Draw")
            print()
        elif Player1 > Player2:
            Player1wins = Player1wins + 1
            print("Player1 wins")
            print()
        else:
            Player2wins = Player2wins + 1
            print("Player2 wins")
            print()
        rounds = rounds + 1
        sleep(1)
    if Player1wins == Player2wins:
        print("Draw")
    elif Player1wins > Player2wins:
        print("Player1 Wins the series")
    elif Player2wins > Player1wins:
        print("Player2 wins the series")


def roll():
    DiceRoll = random.randint(1,6)
    return DiceRoll


main()

