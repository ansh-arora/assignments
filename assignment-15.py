

#Q1
f=open('passage.txt','r')
lines=f.readlines()
length=len(lines)
x=int(input("enter the no. of lines to be printed(from last)"))
h=length-x
for p in range (h,length):
    print(lines[p])
f.close()

#Q2
s=input("enter the word to be counted")
with open('passage.txt', 'r') as f:
    count = 0
    data = f.readlines()
    for line in data:
        words = line.split()
        w = len(words)
        for x in range(0, w):
            if words[x] == s:
                count += 1
    print(count)

#Q3
with open('passage.txt','r') as f, open('passage2.txt','w') as f2:
    file=f.read()
    f2.write(file)
f3=open('passage2.txt','r')
print(f3.read())

#Q4
with open('passage.txt','r') as f,open ('passage2.txt','r') as f2, open ('passage3.txt','w')as f3:
    c=f.readlines()
    l=len(c)
    c2=f2.readlines()
    for x in range (0,l):
        f3.write(c[x]+c2[x])
f3=open('passage3.txt','r')
print(f3.read())


#Q5
import random
f=open('r.txt','w')
for x in range (10):
    s=str(random.randint(0,1000))
    f.write(s+'\t')

f.close()
f=open('r.txt','r')
for n in f:
    l=n.split()
l.sort()
print(l)

