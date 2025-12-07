# def calc_multiple(num1, num2, num3=1):
#     print(f"calculating num1 multiple by num2")
#     if num1 >0 and num2 >0 :
#         result = num1 * num2 * num3
#     print(f"the value of num1 multiplied by num2 is: {result}")
#
#     return result
#
# var1 = 4
# var2 = 5
#
# calc_multiple(var1, var2, 8)

def prices_printing(price):
    if 0<price<100:
        print(f"the price is {price}")

    elif  100<price<1000:
        price = price + 20
        print(f"the new price is {price}")

    elif price > 1000:
        price = price + 50
        print(f"the price is {price}")

    else:
        print(f"invalid input")
    return price


prices_printing(-2)
new_price = prices_printing(44)
if new_price%2 == 0:
    print("the price is even")
else:
    print("the price is odd")

prices_printing(770)
prices_printing(1500)




