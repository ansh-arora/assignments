#Q1
#ZeroDivisionError
a=3
try:
    if a<4:
        a=a/(a-3)
    print(a)
except ZeroDivisionError:
    print("Error: Can't divide by Zero")

#Q2
#IndexError
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("please enter a valid index number")

#Q3
#An exception
#NameError: Hi there

#Q4
# -5.0
# a/b result in 0

#Q5
#1.
try:
    import factorial
    print(factorial(5))
except ModuleNotFoundError:
    print("please enter a valid module")

#2.
try:
    x=int(input("enter integer"))
    print("integer is",x)
except ValueError:
    print("enter a valid integer !!")

#3.
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("please enter a valid index number")

#Q6
class AgeTooSmallError(Exception):
    pass
while True:
    age = int(input("enter age:"))
    try:
        if age>=18:
            print("YOUR AGE IS PERFECT")
            break
        else:
            raise AgeTooSmallError
    except AgeTooSmallError:
        print("YOU ARE UNDER AGE. PLEASE ENTER AGAIN.")
