## Dice.py
## Name
## Date
##
## Dice.py Part 1 will represent a user-input number of rolls of a normal 6-sided dice. 
## Dice.py Part 2 will represent a dice with a user-input number of sides to be rolled. Will continue to roll until the highest number is rolled. 


import random

def dice1():
  ## code for part 1 goes here
    choice = "y"

    while choice == "y":
        dice_six = random.randint(1,6)
        print("Roll result:", dice_six)
        choice = input("Do you want to roll again? (y/n): ")

    print("K. Bye")


def dice2():
  ## code for part 2 goes here
  pass


# call each function to run
dice1()
# dice2()


