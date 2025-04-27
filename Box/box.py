class Box :
    def __init__(self, number, value):
        self.number = number
        self.value = value

    def __repr__(self):
        return f"Box number {self.number} with a value of {self.value}"