from GameFunctions import gamefunctions
from Setup import setup

def play():
    choice = gamefunctions.makechoice()

    boxes = {1: 10, 2: 11, 3: 12}

    while len(boxes) > 0:
        print("Boxes left: ")

        for box in boxes:
            print(box)

        decidedbox = input("Please choose a box to remove: ")

        while not gamefunctions.validateinput(decidedbox):
            decidedbox = input("Invalid selection. Please choose a box to remove: ")

        gamefunctions.removebox(boxes, int(decidedbox))


    end = input("Y/N to end game or loop: ").upper()

    while end != "Y" and end != "N":
        end = input("Sorry try again: ")

    if end == "Y":
        return True
    else:
        return False