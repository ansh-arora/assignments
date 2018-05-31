#Q1
x=input("enter first list element")
y=input("enter second list element")
z=input("enter third list element")
w=[x,y,z]
print(w)
#Q2
companies=['google','apple','facebook','microsoft','tesla']
w.extend(companies)
print(w)
#Q3
print("no.of times 'google' occurs-", w.count("google"))
#Q4
list=[54,12,68,91,0]
print("original list-",list)
list.sort()
print("list in ascending order-",list)
list.reverse()
print("list in descending order-",list)
#Q5
A=[0,2,4,6,8]
B=[1,3,5,7,9]
A.extend(B)
C=A
C.sort()
print(C)
#Q6 stack
a=[]
for x in range (0,5):
 b=input("enter list element")
 a.insert(x,b)
print("list is-",a)
x=4
while x>=0:
    a.pop()
    print("list after deletion-",a)
    x=x-1
#Q6 queue
c=[]
for x in range (0,5):
 d=input("enter list element")
 c.insert(x,d)
print("list is-",c)
x=4
while x>=0:
    c.pop(0)
    x=x-1
    print("list after deletion-",c)
#Q7 optional
n=[2,12,21,30,41,52,6,7,8,9]
even=0
odd=0
print("list is-",n)
for x in range (0,10):
    if n[x]%2==0:
        even=even+1
    else:
        odd=odd+1
print("no.of even numbers-",even)
print("no.of odd numbers-",odd)







