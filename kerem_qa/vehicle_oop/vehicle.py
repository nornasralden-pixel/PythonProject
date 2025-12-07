
class Vehicle:
    def __init__(self):
        print("into vehicle class")

    def ticket_price(self,distance):
        if distance > 100:
            print("you should pay the ticket")



    def calc_distance(self,time,speed):
        print(f"in clac distance with {time} , {speed}")
        distance = speed * time

        return distance

