from kerem_qa.vehicle_oop.car import Car
from kerem_qa.vehicle_oop.motorcycle import motorcycle
from kerem_qa.vehicle_oop.train import Train
from kerem_qa.vehicle_oop.vehicle import Vehicle

car1 = Car(2023,"BMW")
car2 = Car(2020,"cheery")
motor_1 = motorcycle()
train = Train(True)
vehicle = Vehicle()

car1.car_tax_calc(3,120000)
distance_1 = car2.calc_distance(1,60)
distance_train = train.calc_distance(1 , 140)
motor_1.tax_calc(7, 45, 80000)
vehicle.ticket_price(distance_1)
vehicle.ticket_price(distance_train)
car1.get_years(2025)


print("***TEST END***")
