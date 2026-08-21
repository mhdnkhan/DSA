def print_n_to_1(i,n):
    if i<1:
        return
    print(i)
    print_n_to_1(i-1,n)

def main():
    n=int(input("enter the range: "))
    print_n_to_1(n,n)

main()