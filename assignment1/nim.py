#
# You need to replace 'pass' with your code
#

#PLEASE READ: I'm getting errors from the randomizer! I was unable to finish the code because I got random errors, sometimes because of the code, sometimes because of a crash. What is missing is a simple verification for the user input (I tested with legal inputs, still crashes). 

from random import randint
from math import log

# Define constant variables.


# Create the initial pile, determine the starting player and the computer's
# strategy.
HUMAN = 0
COMPUTER = 1
SMART = 0
DUMB = 1


def nim():
    """
    return True if the winner is human, False if winner is computer.
    """
    pile = randint(10, 100)
    turn = randint(0, 1)
    strategy = randint(0, 1)
    while pile > 0:
        if turn == COMPUTER:
            if pile == 1:
                take = 1
            elif strategy == DUMB:
                take = randint(1,(pile/2))
            elif pile == 3 or pile == 7 or pile == 15 or pile == 31 or pile == 63:
                take = randint(1,(pile/2))
            elif pile > 63:
                take = pile - 63
            elif pile > 31:
                take = pile - 31
            elif pile > 15:
                take = pile - 15
            elif pile > 7:
                take = pile - 7
            elif pile > 3:
                take = pile - 3
            pile = pile - take
            print("The computer took %d marbles, leaving %d.\n" % (take, pile))
            turn = HUMAN
        elif turn == HUMAN:
            print("Your turn.   The pile currently has", pile, "marbles in it.")
            take = int(input("How many marbles will you take? "))
            pile = pile - take
            print("Now the pile has", pile, "marbles in it.\n")
            turn = COMPUTER

    return turn == COMPUTER

if nim():
    print("You Won!")
else:
    print("The computer won!")