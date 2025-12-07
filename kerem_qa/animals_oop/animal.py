class Animal:
    def __init__(self):
        pass
        # print("into animal constructor")

    def make_sound(self, sound):
        print(f"the animal makes sound {sound}")

    def get_legs_from_db_into_animal(self, legs_amount):
        if legs_amount == 4:
            print("you has 4 legs")

        else:
            legs_amount = 4
            print("legs changed to 4 legs")
        return legs_amount

