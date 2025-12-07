from kerem_qa.vehicle_oop.vehicle import Vehicle


class motorcycle(Vehicle):
    def __init__(self):
        pass

    def tax_calc(self, year, tax_value, price):
        if year>5:
            price = price + tax_value
            print(f"motorcycle price is {price}")
            return price