n=int(input())
digits= len(str(n))
temp=n
total=0
while temp>0:
    d=temp%10
    total+= d**digits
    temp//=10
if total==n:
    print("armstrong")
else:
    print("not armstrong")