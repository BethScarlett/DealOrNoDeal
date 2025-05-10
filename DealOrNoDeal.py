from GameFunctions.gamefunctions import offertwentythree
from Setup import *
from GameplayLoop import play

if __name__ == '__main__':
    i = 0
    while i < 20:
        test = offertwentythree(100)
        print(test)
        i+= 1
    name = input("Welcome. What is your name? ")

    print(f"Hello {name}. It's time to play deal or no deal.")

    while play.play():
        print("Looping again...")