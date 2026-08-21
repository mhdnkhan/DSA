def sum(i,s):
    if i<1:
        print(s)
        return
    sum(i-1,s+i)

def main():
    n=int(input())
    sum(n,0)

main()