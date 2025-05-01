from GameFunctions import gamefunctions
from Setup import setup

def play():
    choice = gamefunctions.makechoice()

    boxes = setup.setupboxes()
    count : int = 1

    while not boxes.get(choice):
        print("Sorry box doesn't exist.")
        choice = gamefunctions.makechoice()

    gamefunctions.removebox(boxes, int(choice))

    while len(boxes) > 0:
        print("Boxes left: ")

        for box in boxes:
            print(boxes[box])

        decidedbox = input("Please choose a box to remove: ")

        while not gamefunctions.validateinput(decidedbox):
            decidedbox = input("Invalid selection. Please choose a box to remove: ")

        result = gamefunctions.removebox(boxes, int(decidedbox))

        if result and len(boxes) > 1:
            if count == 4:
                print(f"Offer of £{gamefunctions.makeoffer(boxes)}")
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