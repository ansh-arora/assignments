#Q1
tuple1=(1,'hello',9.0,34,'c')
print(tuple1)
print("length of tuple-",len(tuple1))


#Q2
#tuple of string
tuple2=('hello','up','google','zoom')
print("tuple is-",tuple2)
print("max element-",max(tuple2))
#tuple of numbers
tuple3=(1,27,4,31,31.1)
print("tuple is-",tuple3)
print("max element-",max(tuple3))


#Q3
tuple4=(3,2,5,4)
print("tuple is-",tuple4)
i=1
i=tuple4[0]*tuple4[1]*tuple4[2]*tuple4[3]
print("product=",i)

#SETS
#Q1
set1=set()
x=input("enter elements of first set")
set1.add(x)
x=input("enter elements of first set")
set1.add(x)
x=input("enter elements of first set")
set1.add(x)
set2=set()
x=input("enter elements of second set")
set2.add(x)
x=input("enter elements of second set")
set2.add(x)
x=input("enter elements of second set")
set2.add(x)
print("set 1 is-",set1)
print("set 2 is-",set2)
x= set1 >= set2
print("is set1 superset of set2-",x)
x=set1 <= set2
print("is set2 superset of set1-",x)
set3= set1&set2
print("intersection of set1 and set2-",set3)


#DICT
#Q1

dict1={}
dict1['name1']=input("student 1 name")
dict1['name2']=input("student 2 name")
dict1['name3']=input("student 3 name")
dict1['name4']=input("student 4 name")
dict1['name5']=input("student 5 name")
dict1['name6']=input("student 6 name")
dict1['name7']=input("student 7 name")
dict1['name8']=input("student 8 name")
dict1['name9']=input("student 9 name")
dict1['name10']=input("student 10 name")
dict1['marks1']=input("student 1 marks")
dict1['marks2']=input("student 2 marks")
dict1['marks3']=input("student 3 marks")
dict1['marks4']=input("student 4 marks")
dict1['marks5']=input("student 5 marks")
dict1['marks6']=input("student 6 marks")
dict1['marks7']=input("student 7 marks")
dict1['marks8']=input("student 8 marks")
dict1['marks9']=input("student 9 marks")
dict1['marks10']=input("student 10 marks")


#Q3
c="MISSISSIPPI"
d={}
d['M']=(c.count("M"))
d['I']=c.count("I")
d['S']=c.count("S")
d['P']=c.count("P")
print("no.of repetitions is:",d)

#Q2





