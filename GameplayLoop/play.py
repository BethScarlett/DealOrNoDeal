from Box.box import Box
from GameFunctions import gamefunctions
from Setup import setup

def play():
    choice = gamefunctions.makechoice()

    boxes = setup.setupboxes()
    count : int = 1
    acceptoffer : bool = False

    while not boxes.get(choice):
        print("Sorry, but box doesn't exist.")
        choice = gamefunctions.makechoice()

    userbox : Box = boxes[choice]
    gamefunctions.removebox(boxes, int(choice))

    availablenums = ["1p", "10p", "50p", "£1", "£2", "£5", "£10", "£50", "£100", "£250", "£500", "£750",
                     "£1,000", "£3,000", "£5,000", "£10,000", "£15,000", "£20,000", "£35,000",
                     "£50,000", "£75,000", "£100,000", "£250,000"]

    while len(boxes) > 1 and not acceptoffer:
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

            amount = str(boxes[decidedbox])
            i = str(boxes[decidedbox]).index("of")
            availablenums.remove(amount[i + 3:])

            result = gamefunctions.removebox(boxes, decidedbox)

            if result and len(boxes) > 1:
                if count == 4:
                    offer = gamefunctions.makeoffer(boxes, userbox.value)
                    print(f"Offer of £{offer}")
                    acceptoffer = gamefunctions.acceptoffer(offer)
                    count = 1
                else:
                    print("Let's go again")
                    count += 1
        except KeyError:
            print("I'm sorry, but the box you've chosen has already been removed from the pool.")
    last_box = None
    for box in boxes:
        last_box = boxes[box]

    endgame(last_box, userbox)

    #print("You had " + str(userbox))
    end = input("Y/N to end game or loop: ").upper()

    while end != "Y" and end != "N":
        end = input("Sorry try again: ").upper()

    if end == "Y":
        return True
    else:
        return False

def endgame(last_box, userbox):
    print(last_box)
    print(userbox)
    final_box : Box = gamefunctions.swapbox(last_box, userbox)
    print(final_box)

    final_box.value = gamefunctions.offertwentythree(final_box.value)

    print(f"You have won £{int(final_box.value / 100)}")