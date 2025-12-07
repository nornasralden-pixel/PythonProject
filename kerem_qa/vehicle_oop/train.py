from kerem_qa.vehicle_oop.vehicle import Vehicle


class Train(Vehicle):
    def __init__(self, is_light):
        self.is_light = is_light

    def get_passenger(self,train_cars):
        passenger = train_cars * 50
        print(f"max amount of passenger is {passenger}")


