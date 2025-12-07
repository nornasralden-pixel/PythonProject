Name = "Noor"
Name_len = len(Name)

if(Name == "Noor"):
    print("Name found")
else:
    print("Name not found")

if (Name_len < 3):
    print("Name too short")
elif (Name_len < 5):
    print("Name is meduim")
else:
    print("Name is too long")