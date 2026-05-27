class House:
    def __init__(self, color, size, price):
        self.color = color
        self.size = size
        self.price = price

    def display_info(self):
        print(f"This house is {self.color}, has a size of {self.size} square feet, and costs ${self.price}.")
        