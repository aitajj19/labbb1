
import math
p=0
eps=0.001
x=0.5
a=math.sin(x)
a1=1
p=0
n=2
while abs((a/a1))>eps:
    a=(-1)**(n-1)*math.sin(x)**n
    a1=a1*n
    p+=a/a1
    n+=1
print("p=",p)