full_name = "Noor Nsr aldean"

index_1 = full_name.index(" ")
# index_2 = full_name.index(" ",index_1+1,full_name_length-1)
full_name_length= len(full_name)
first_name = full_name[0:index_1]
first_name_by_slicing = first_name[:full_name_length]

last_name=full_name[index_1:full_name_length]
last_name_by_slicing = full_name[index_1:]
print(F"last name is #{last_name}#")
print(first_name)
index_2 = full_name.index(" ")
sentens= " hi my name is noor , i live in dalyatalcarmel , the place dalya best"
index_3 = sentens.index("place")+6
place = sentens[index_3:-5]

print("test end")