# Caculator 1 to calculate 47 and 7
#Author: Baiying Lu, NetID: bl223

#This function is to do addition
def add(x,y):
    c = x+y
    symbol = "+"
    return c, symbol

#This function is to do substraction
def substract(x,y):
    c = x-y
    symbol = "-"
    return c, symbol

#This function is to do multiplication
def multiply(x,y):
    c = x*y
    symbol = "*"
    return c, symbol

#This function is to do division
def divide(x,y):
    c = x/y
    symbol = "/"
    return c, symbol

message = "Enter a letter to calculate 47_7=?\n\
'a' means add, 's' means substract, 'm' means multiply, 'd' means divide\n\
Enter the action you want to do:\n"
x = input(message)
print("You entered {}".format(x))
number1 = 47
number2 = 7
if x == "a":
    result,action = add(number1,number2)
    print("{} {} {} = {}".format(number1,action,number2,result))

elif x == "s":
    result,action = substract(number1,number2)
    print("{} {} {} = {}".format(number1,action,number2,result))

elif x =="m":
    result,action = multiply(number1,number2)
    print("{} {} {} = {}".format(number1,action,number2,result))

elif x =="d":
    result,action = divide(number1,number2)
    print("{} {} {} = {}".format(number1,action,number2,result))

else:
    print("The {} command is not recognized.".format(x))
print("Done")
