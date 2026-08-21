def print_1_to_n(i,n):
    if i<1:
        return
    print_1_to_n(i-1,n)
    print(i)

def main():
    n=int(input("enter the range: "))
    print_1_to_n(n,n)

main()