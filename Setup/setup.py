import random
from Box.box import Box


def setupboxes():
    boxes = {}
    values = [1, 10, 50, 100, 500, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 300000, 500000, 1000000,
              1500000, 2000000, 3500000, 5000000, 7500000, 10000000, 25000000]
    for i in range(1, len(values) + 1):
        value = random.choice(values)
        newbox = Box(i, value)
        boxes[i] = newbox
        values.remove(value)

    return boxes