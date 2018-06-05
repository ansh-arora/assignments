#Q1
l=[]
for x in range (10):
    c=int(input("enter number"))
    l.append(c)
for x in range (10):
    print("number",x+1,":",l[x])

#Q2
=0
while c>=0:
    print("number is:",c)

#Q3
l1=[]
l2=[]
for x in range (5):
    c=int(input("enter number:"))
    l1.append(c)
    c=c*c
    l2.append(c)
print("numbers:",l1)
print("square of numbers:",l2)

#Q4
l3=[5,5.5,'hi','yo',60,80.0]
lint=[]
lstring=[]
lfloat=[]
d=len(l3)
for x in range (d):
    if type(l3[x])==float:
        lfloat.append(l3[x])
    elif type(l3[x])==int:
        lint.append(l3[x])
    else:
        lstring.append(l3[x])
print("integers are:",lint)
print("float are:",lfloat)
print("string are",lstring)

#Q5
lprime=[]
for x in range (1,102):
    s=0
    for j in range (1,x+1):
        if(x%j==0):
            s+=1
    if s ==2:
        lprime.append(x)
print("prime numbers between 1 to 101 are:",lprime)

#Q6
for x in range(1,5):
    for y in range (x):
        print("*",end='')
    print()

#Q7
di=dict()
for x in range (5):
    c=input("enter key")
    di[c]=input("enter value")
for x in di:
    print(x,":",end='')
    print(di[x])

#Q8
l6=[]
for x in range (5):
    c=input("enter elements of list")
    l6.append(c)
print("list is:",l6)
p=input("enter element to be deleted")
b=0
for x in range(5):
    if p==l6[x]:
        l6.remove(p)
        b+=1
        break
if b==1:
    print("new list is:",l6)
else:
    print("**ELEMENT NOT FOUND**")

