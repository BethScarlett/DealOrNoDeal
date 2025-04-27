def validateinput(choice):
    if not choice.isdigit():
        return False

    choice = int(choice)

    if choice < 1 or choice > 22:
        return False

    return True

def removebox(boxes, choice):
    try:
        print(boxes[choice])
        boxes.pop(choice)
    except KeyError:
        print("Sorry I can't find that box.")

def makechoice():
    choice = input("To begin, please select a box number between 1 and 22: ")

    while not validateinput(choice):
        choice = input("I'm sorry that's not a valid input. please select a box number between 1 "
                       "and 22: ")

    return int(choice)