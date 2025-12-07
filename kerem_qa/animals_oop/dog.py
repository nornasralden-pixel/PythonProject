from kerem_qa.animals_oop.animal import Animal


class Dog(Animal):
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def get_eyes_color(self , eye_color="Gray"):
        print(f"the dog eyes has color {eye_color}")

    def get_legs_from_db(self, legs_amount):
        if legs_amount == 4:
            print("you have 4 legs")

        else:
            legs_amount = 4
            print("legs changed to 4 legs")
        return legs_amount