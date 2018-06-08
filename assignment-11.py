#Q1
class Animal:
     def animal_attribute(self):
         print("animals: multicellular & eukaryotic")


class tiger(Animal):
     def family(self):
         print("family of cats")
     def feed(self):
         print("produce milk")
t=tiger()
t.animal_attribute()
t.family()
t.feed()

#Q2
#output is: A B

#Q3
class cops:
    def __init__(self):
        self.name='naresh'
        self.age=32
        self.exp=10
        self.desig='constable'
    def update(self,n,a,e,d):
        self.name = n
        self.age = a
        self.exp = e
        self.desig = d

class mission(cops):
    def add_mission_details(self,l,t):
        self.loc=l
        self.time=t
    def dis(self):
        print("name:",self.name,"\nage:",self.age,"\nwork experience:",self.exp,"\ndesignation:",self.desig,"\nlocation:",self.loc,"\ntime:",self.time)
c1=cops()
m1=mission()
m1.add_mission_details('goa','3months')
m1.dis()


#Q4
class shape:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
         self.a=self.length*self.breadth
         print(self.a)
class square(shape):
    def dis(self):
        print("area of square:")
class rectangle(shape):
    def dis(self):
        print("area of rectangle:")

s=square(3,3)
s.dis()
s.area()
r=rectangle(2,5)
r.dis()
r.area()




