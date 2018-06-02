#Q1
x=int(input("enter year to be checked"))
if x%100==0:
    if x%400==0:
        print("!! LEAP YEAR !!")
    else:
        print("xx NOT A LEAP YEAR xx")
elif x%4==0:
    print("!! LEAP YEAR !!")
else:
    print("xx NOT A LEAP YEAR xx")

#Q2
y=int(input("enter length of shape"))
z=int(input("enter breadth of shape"))
if y==z:
    print("!! IT IS A SQUARE !!")
else:
    print("!! IT IS A RECTANGLE !!")


#Q3
a1=int(input("enter age of first person"))
a2=int(input("enter age of second person"))
a3=int(input("enter age of third person"))
if a1>a2 and a1>a3:
    print("first person age-",a1," is eldest")
    if a2>a3:
        print("third person age-",a3," is youngest")
    else:
        print("second person age-", a2, " is youngest")
elif a2>a1 and a2>a3:
    print("second person age-", a2, " is eldest")
    if a1 > a3:
        print("third person age-", a3, " is youngest")
    else:
        print("first person age-", a1, " is youngest")
elif a3>a2 and a3>a1:
    print("third person age-",a3," is the eldest")
    if a1>a2:
        print("second person age-",a2," is the youngest")
    else:
        print("first person age-", a1, " is youngest")
else:
    print("**ALL ARE OF SAME AGE**")

#Q4
age=int(input("enter age of employee"))
sex=input("GENDER -'M' for MALE & 'F' for FEMALE")
mar=input("MARITAL STATUS- 'Y' for YES & 'N' for NO")
if sex=='F':
    print("employee will work in 'URBAN AREA'")
else:
    if age>=20 and age<40:
        print("employee will work ANYWHERE")
    elif age>=40 and age<=60:
        print("employee will work in 'URBAN AREA'")
    else:
        print("!! ERROR !! ENTER VALID AGE !!")
#Q5
q=int(input("enter quantity purchased"))
c=100*q
if c>1000:
    c=c-(0.1*c)
    print("!! YOU WILL GET 10% DISCOUNT !! FINAL PRICE- RS.",c)
else:
    print("!! SORRY !! NO DISCOUNT !! FINAL PRICE- RS.",c)


