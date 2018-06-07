#Q1 time-tuple: shows current time in the form of a tuple having 9 values like month,year,day,hours,seconds etc
import time
print("Time tuple (acc. to UTC):")
print(time.gmtime())

#Q2
t=time.gmtime()
print("Current UTC time:",end="")
print(time.asctime(t))

#Q3
import datetime
from datetime import date
d=date.today()
print("today's date:",d)
print("month:",d.month)

#Q4,#Q5
print("day:",d.day)

#Q6
print("Local time:",end="")
print(time.ctime())

#Q7
f=int(input("enter number:"))
import math
print("factorial of ",f,":",math.factorial(f))

#Q8
g=int(input("enter number 1:"))
g1=int(input("enter number 2:"))
print("GCD of ",g,"and",g1,":",math.gcd(g,g1))

#Q9
import os
print("current working directory: ",os.getcwd())
print("User environment: ",os.environ)

