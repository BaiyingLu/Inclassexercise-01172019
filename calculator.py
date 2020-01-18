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

x = input("Enter a letter to calculate 47_7=?\n'a' means add, 's' means substract, 'm' means multiply, 'd' means divide\nEnter the action you want to do:\n") #stop and wait the input <br>a means add, s means substract, m means multiply, d means divide<br>Enter the action you want to do
print("You entered {}".format(x))
if x == "a":
    result,action = add(47,7)
    print("{} {} {} = {}".format(47,action,7,result))

elif x == "s":
    result,action = substract(47,7)
    print("{} {} {} = {}".format(47,action,7,result))

elif x =="m":
    result,action = multiply(47,7)
    print("{} {} {} = {}".format(47,action,7,result))

elif x =="d":
    result,action = divide(47,7)
    print("{} {} {} = {}".format(47,action,7,result))

else:
    print("The {} command is not recognized.".format(x))
print("Done")
