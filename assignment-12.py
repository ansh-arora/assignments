#Q1
import time
import threading
from threading import Thread

def sample():
     print("HI !!")
     time.sleep(5)
     print("BYE !!")
s=Thread(target=sample)
s.start()

#Q2
def numbers(x):
    print(x)

for x in range (1,11):
    n1=Thread(target=numbers,args=[x])
    time.sleep(1)
    n1.start()

#Q3
l=['2','4','6','8','10']
def numbers(x):
    print(x)

delay=2
for x in range (0,5):
    n1=Thread(target=numbers,args=[l[x]])
    time.sleep(delay)
    delay += 2
    n1.start()

#Q4
import math
def factorial(z):
    t=math.factorial(z)
    print("factorial is:",t)

c=int(input("enter number"))
r=Thread(target=factorial,args=[c])
r.start()






