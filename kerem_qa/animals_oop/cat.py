from kerem_qa.animals_oop.animal import Animal


class Cat(Animal):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_legs_from_db(self, legs_amount):
        if legs_amount == 4 :
            print("You have 4 legs")

        else:
            legs_amount = 4
            print("legs changed to 4 legs")
        return legs_amount

    def make_noise_by_cat(self):
        print("meow")
