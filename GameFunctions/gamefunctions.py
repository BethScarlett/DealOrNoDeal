########## Validation ##########
import random


def validateinput(choice):
    if not choice.isdigit():
        return False

    choice = int(choice)

    if (choice < 1 or choice > 24) or choice == 23:
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
    choice = input("To begin, please select a box number between 1 and 24, excluding 23: ")

    while not validateinput(choice):
        choice = input("I'm sorry that's not a valid input. please select a box number between 1 "
                       "and 24, excluding 23: ")

    return int(choice)

def swapbox(rem_box, user_box):
    swap = input("Would you like to swap boxes (Y/N)? ").upper()

    if swap == "Y":
        return rem_box
    else:
        return user_box

########## OFFER ##########

def makeoffer(boxes, userbox):
    offer = 0.00
    for box in boxes:
        offer += boxes[box].value

    offer = ((offer + userbox) / len(boxes) + 1)/100

    if offer < 1:
        offer = round(offer, 2)
    else:
        offer = int(offer)

    return offer

def acceptoffer(offer) -> bool:
    decision = input("Would you like to accept this offer (Y/N)? ").upper()

    while decision != "Y" and decision != "N":
        decision = input("Sorry I didn't quite catch that. Try again: ").upper()

    if decision == "Y":
        print(f"You have accepted the offer. Congratulations you've won £{offer}.")
        return True
    else:
        return False

########## BOX 23 ##########

def offertwentythree(winnings):
    #Box 23 can either double money, half money, lose all money, add £10,000 or do nothing
    choice = input("Will you take box 23? ").upper()
    if choice == "Y":
        gamble = ["Double", "Half", "Empty", "Add", "None"]
        outcome = random.choice(gamble)
        match outcome:
            case "Double":
                winnings *= 2
                return winnings
            case "Half":
                winnings /= 2
                return int(winnings)
            case "Empty":
                return 0
            case "Add":
                winnings += 10000
                return winnings
            case default:
                return winnings
    else:
        return winnings

