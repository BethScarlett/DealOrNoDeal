from GameFunctions import gamefunctions
from Setup import setup

def play():
    choice = gamefunctions.makechoice()

    #boxes = {1: 10, 2: 11, 3: 12, 4: 13, 5: 15}
    boxes = setup.setupboxes()
    count : int = 0

    while len(boxes) > 0:
        print("Boxes left: ")

        for box in boxes:
            print(box)

        decidedbox = input("Please choose a box to remove: ")

        while not gamefunctions.validateinput(decidedbox):
            decidedbox = input("Invalid selection. Please choose a box to remove: ")

        gamefunctions.removebox(boxes, int(decidedbox))
        if count == 4:
            print("Making Offer")
            count = 1
        else :
            print ("Let's go again")
            count += 1


    end = input("Y/N to end game or loop: ").upper()

    while end != "Y" and end != "N":
        end = input("Sorry try again: ")

    if end == "Y":
        return True
    else:
        return False