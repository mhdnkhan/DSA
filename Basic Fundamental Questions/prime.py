n= int(input("enter a number: "))
if n<=1:
    print("not prime")
else:
    prime= True
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            prime= False
            break
    if prime:
        print("prime")
    else:
        print("not prime")