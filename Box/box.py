class Box :
    def __init__(self, number, value):
        self.number = number
        self.value = value

    def __repr__(self):
        if self.value < 99:
            repval = f"{self.value}p"
        else :
            repval = f"£{int(self.value / 100):,}"
        return f"Box number {self.number} with a value of {repval}"