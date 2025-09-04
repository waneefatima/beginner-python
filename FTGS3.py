def goto1():
    print(num1+num2)
def goto2():
    print(num1-num2)
def goto3():
    print(num1/num2)
num1 =int(input("enter your first number "))
num2 =int(input("enter your second number "))

res =str(input("enter the calculations you would like to do"))
if res == "addition" :
    goto1()
elif res == "subtraction":
    goto2()
elif res == "division" :
    goto3()
elif res == "multiplication":
    print (num1/num2)
#updated hello.py
