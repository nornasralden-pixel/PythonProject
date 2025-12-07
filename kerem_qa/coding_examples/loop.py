

# num = 3
# for i in range(1,11):
#     print(num*i)
#     summery= num*i
#     if(summery % 2 == 0):
#         print(F"the number {summery} is even")
#
# num1= 3
# num2= 5
# summery = num1 + num2
# if summery % 2 == 0:
#     print(summery)

num1 = 10
cntr = 100
i =3
is_dived = True
while(is_dived == True):
    # handing case of infinity by decreased counter to 100
    cntr -= 1
    print(f"counter value is {cntr}")
    if(cntr == 0):
        break
    result = num1%i
    i+=1
    if (result == 0):
        is_dived = False
        print(f" the result of deived in {i-1} is 0")



