from kerem_qa.animals_oop.cat import Cat
from kerem_qa.animals_oop.dog import Dog

cat_1 = Cat("liz" , "white")
cat_2 = Cat("lily" , "black")
dog_1 = Dog("shoko" , "5")


cat_1.make_noise_by_cat()
cat_2.make_noise_by_cat()
cat_legs = cat_1.get_legs_from_db(3)
dog_legs = dog_1.get_legs_from_db(5)
cat_1.get_legs_from_db_into_animal(4)
dog_1.make_sound("hao")
if cat_legs == dog_legs:
    print("legs amount is equal")


dog_1.get_eyes_color()
