# This is an advanced calculatory
#This function is to do addition
def add(x,y):
    c = x+y
    symbol = "+"
    c = round(c,3)
    return c, symbol

#This function is to do substraction
def substract(x,y):
    c = x-y
    symbol = "-"
    c = round(c,3)
    return c, symbol

#This function is to do multiplication
def multiply(x,y):
    c = x*y
    symbol = "*"
    c = round(c,3)
    return c, symbol

#This function is to do division
def divide(x,y):
    c = x/y
    symbol = "/"
    c = round(c,3)
    return c, symbol

#Enter the calculation method
x = input("Enter a letter to decide calucation method\n'a' means add, 's' means substract, 'm' means multiply, 'd' means divide\nEnter the action you want to do:\n") #stop and wait the input <br>a means add, s means substract, m means multiply, d means divide<br>Enter the action you want to do
print("You entered {}".format(x))

#Input the first number and str2num
input1 = input("Enter the first number:")
print("The first number you entered is {}".format(input1))
number1 = float(input1)

#Input the second number and str2num
input2 = input("Enter the second number:")
print("The second number you entered is {}".format(input2))
number2 = float(input2)

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
