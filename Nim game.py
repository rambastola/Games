# Ram Bastola
# Nim game
# Player vs computer.

import random
import time

def user():
    """
    ask user how many balls they want to play with and the whole strategies of game.
    - player 1 starts the game and make a first choice
    """

    user1 = int(input("How many balls do you want to play with? "))
    rem_balls = user1

# forcing player to play with more than 15 balls
    while rem_balls <15:
        user1 = int(input("Try Again! You need at least 15 or higher number of balls to start the game "))
        rem_balls = user1

    #    User cannot pick more than 4 balls
    #    User cannot pick 0 balls
    while rem_balls > 4:
        
        if rem_balls % 5 == 0:

            user11 = int(input("Pick number of balls between 1-4 "))
            while user11 > 4 or user11 == 0:
                user11 = int(input("Pick number of balls between 1-4 "))
            rem_balls = rem_balls - user11
            print("Remaining balls are",rem_balls)

        # if remainder is 0, computer picks random number of balls
            if rem_balls % 5 == 0:
                comp_pick = random.randint(1, 4)

        # if there is a remainder, computer picks the remainder to make it multiple of 5
            else:
                comp_pick = rem_balls % 5
            rem_balls = rem_balls - comp_pick
            print("computer chose",comp_pick, "balls" )
            print("Remaining balls", rem_balls)

        # if all bals are picked
            while rem_balls <= 0:
                print("Computer has won, be better prepared next time :) !")
                break

    # for user when it's a number not divisible by 5
        elif rem_balls % 5 != 0:
            user11 = int(input("Choose number of balls between 1-4 "))
            rem_balls = rem_balls - user11
            print("Remaining balls are", rem_balls)
            if rem_balls <= 4:
                print("You win")

#if it's computer's turn and there is no remainder
            comp_pick = rem_balls % 5
            if comp_pick == 0:
                comp_pick = random.randint(1, 4)
            rem_balls = rem_balls - comp_pick
            print("Computer chose",comp_pick, "balls")
            print("Remaining balls = ", rem_balls)
            if rem_balls <= 4:
                user11 = int(input("Choose number of balls between 1-4 "))
                if user11 == rem_balls:
                    print("You've picked all the balls, you win")
                if user11 != rem_balls:
                    comp_pick = rem_balls - user11
                    print("Computer has picked the", comp_pick,"balls")
                    print("You lost. Be better prepared next time. :)")
    
    #calling it on main function
def main():

    print("Welcome to nim game!")
    time.sleep(1)
    print("It's you vs the computer")
    print("Choose at least 15 balls to start the game!")
    print("You can remove up to 4 balls at a time")
    print("Your goal is to get the last ball")
    time.sleep(1)
    user()


main()
