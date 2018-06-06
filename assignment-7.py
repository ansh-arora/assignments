#Q1
r=int(input("enter radius of sphere"))
def area(d):
    a=(4/3)*3.14*d*d*d
    return a
ar=area(r)
print("area of sphere:",ar)


#Q2
def perfect(p):
    x=1
    s=0
    while x<p:
        if(p%x==0):
            s+=x
        x+=1
    if s==p:
        print(p,"is a perfect number")
for x in range (1,1000):
    perfect(x)

#Q3
num=int(input("enter number to write table:"))
def table(x):
    if x == 0:
        return 0
    else:
        sum = num + table(x - 1)
    return sum
for x in range (1,11):
    sum=table(x)
    print(num,"*",x,"=",sum)

#Q4
s=int(input("enter number:"))
p=int(input("enter power:"))
def power(p):
    if p==0:
        return 1
    else:
        return s*power(p-1)

for x in range (1,p+1):
    sq=power(x)
print(s,"^",p,"=",sq)

#Q5
f=int(input("enter number to find factorial:"))
def fact(z):
    x=1
    fc=1
    while x<=z:
        fc=fc*x
        x+=1
    return fc
fc=fact(f)
di=dict()
di[f]=fc
print("factorials are:",di)

