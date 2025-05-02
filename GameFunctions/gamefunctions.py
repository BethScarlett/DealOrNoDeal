########## Validation ##########

def validateinput(choice):
    if not choice.isdigit():
        return False

    choice = int(choice)

    if choice < 1 or choice > 22:
        return False

    return True

########## BOX FUNCTIONS ###########

def removebox(boxes, choice):
    try:
        boxes.pop(choice)
        return True
    except KeyError:
        print("Sorry I can't find that box.")
        return False

def makechoice():
    choice = input("To begin, please select a box number between 1 and 22: ")

    while not validateinput(choice):
        choice = input("I'm sorry that's not a valid input. please select a box number between 1 "
                       "and 22: ")

    return int(choice)

########## OFFER ##########

def makeoffer(boxes):
    offer = 0.00
    for box in boxes:
        offer += boxes[box].value

    offer = (offer / len(boxes))/100

    if offer < 1:
        offer = round(offer, 2)
    else:
        offer = int(offer)

    return offer

def acceptoffer() -> bool:
    decision = input("Would you like to accept this offer (Y/N)? ").upper()

    while decision != "Y" and decision != "N":
        decision = input("Sorry I didn't quite catch that. Try again: ").upper()

    if decision == "Y":
        return True
    else:
        return False