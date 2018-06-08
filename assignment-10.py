#Q1
class circle:
    def getArea(self,r):
        area=3.14*r*r
        print("area is:",area)
    def getCircumference(self,r):
        c=2*3.14*r
        print("circumference is:",c)
x=circle()
s=int(input("enter radius"))
x.getArea(s)
x.getCircumference(s)

#Q2
class student:
    def __init__(self,n,r):
        self.name=n
        self.rno=r
    def dis(self):
        print("name=",self.name)
        print("roll no=",self.rno)
s1=student('ashish',99)
s1.dis()

#Q3
class Temperature:
    def ctof(self,c):
        f=(c*1.8)+32
        print("temperature in fahrenheit:",f)
    def ftoc(self,f):
        c = (f-32)/1.8
        print("temperature in fahrenheit:", c)
t=Temperature()
c=int(input("enter temp in celsius"))
t.ctof(c)
f=int(input("enter temp in fahrehheit"))
t.ftoc(f)

#Q4
class MovieDetails:
    def __init__(self):
        self.name='Yeh jawani hai deewani'
        self.artist='ranbir'
        self.yor=2013
        self.ratings=4
    def update(self,n,a,y,r):
        self.name=n
        self.artist=a
        self.yor=y
        self.ratings=r
    def dis(self):
        print("movie:",self.name, "\nartist:",self.artist, "\nyear of release:",self.yor,
        "\nratings:",self.ratings)
m=MovieDetails()
m.dis()
m.update('sherlock','robert',2012,4)
m.dis()

#Q5
class Expenditure:
    def __init__(self):
        self.expend=5000
        self.savings=1000
    def calc(self):
        self.c=self.expend+self.savings
    def dis(self):
        print("salary :",self.c)
e=Expenditure()
e.calc()
e.dis()







