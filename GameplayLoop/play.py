from GameFunctions import gamefunctions
from Setup import setup

def play():
    choice = gamefunctions.makechoice()

    boxes = setup.setupboxes()
    count : int = 1

    while not boxes.get(choice):
        print("Sorry, but box doesn't exist.")
        choice = gamefunctions.makechoice()

    gamefunctions.removebox(boxes, int(choice))

    availablenums = ["1p", "10p", "50p", "£1", "£5", "£10", "£50", "£100", "£250", "£500", "£750",
                     "£1,000", "£3,000", "£5,000", "£10,000", "£15,000", "£20,000", "£35,000",
                     "£50,000", "£75,000", "£100,000", "£250,000"]

    while len(boxes) > 0:
        print("Boxes left: ")

        for box in boxes:
            print("[" + str(box) + "] ", end='')

        print()

        print("Amounts left: ")

        for x in availablenums:
            print(x + "/ ", end='')

        print()

        decidedbox = input("Please choose a box to remove: ")

        while not gamefunctions.validateinput(decidedbox):
            decidedbox = input("Invalid selection. Please choose a box to remove: ")

        try:
            decidedbox = int(decidedbox)
            print(f"You have chosen: {boxes[decidedbox]}")
            result = gamefunctions.removebox(boxes, decidedbox)

            amount = str(boxes[decidedbox])
            i = str(boxes[decidedbox]).index("of")
            availablenums.remove(amount[i + 3:])

            if result and len(boxes) > 1:
                if count == 4:
                    print(f"Offer of £{gamefunctions.makeoffer(boxes)}")
                    count = 1
                else:
                    print("Let's go again")
                    count += 1
        except KeyError:
            print("I'm sorry, but the box you've chosen has already been removed from the pool.")

    end = input("Y/N to end game or loop: ").upper()

    while end != "Y" and end != "N":
        end = input("Sorry try again: ")

    if end == "Y":
        return True
    else:
        return False