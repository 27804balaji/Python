class car:
    def __init__(self):
        self.brand = input()
        self.price = input()
        self.color = input()

    def choose(self):
        print(self.brand)

class user(car):
    def user_1(self):
        print(self.brand)

obj=car()
obj.choose()

