n=int(input())
a,b=0,1
if n>=1:
    print(a)
if n>=2:
    print(b)
for i in range(3, n+1):
    c=a+b
    print(c)
    a=b
    b=c