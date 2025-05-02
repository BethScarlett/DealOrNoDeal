from Setup import *
from GameplayLoop import play

if __name__ == '__main__':
    name = input("Welcome. What is your name? ")

    print(f"Hello {name}. It's time to play deal or no deal.")

    while play.play():
        print("Looping again...")