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
        print(boxes[choice])
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
    offer = 0
    for box in boxes:
        print("box = " + str(box) + " value = " + str(boxes[box]))
        offer += boxes[box]

    return int(offer / len(boxes))
