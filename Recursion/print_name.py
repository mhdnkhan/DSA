name=input("enter the name: ")
def print_name(i,n):
    if i>n:
        return
    print(name)
    print_name(i+1,n)

def main():
    n=int(input("enter the no. for the range: "))
    print_name(1,n)

main()