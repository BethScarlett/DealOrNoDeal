import random
from Box.box import Box


def setupboxes():
    boxes = {}
    values = ["1p", "10p", "50p", "£1", "£5", "£10", "£50", "£100", "£250", "£500", "£750", "£1,000", "£3,000",
              "£5,000", "£10,000", "£15,000", "£20,000", "£35,000", "£50,000", "£75,000", "£100,000", "£250,000"]
    for i in range(1, len(values) + 1):
        value = random.choice(values)
        newbox = Box(i, value)
        boxes[i] = newbox
        values.remove(value)

    return boxes