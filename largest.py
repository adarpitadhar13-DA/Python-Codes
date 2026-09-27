def find_largest(a,b,c):
    if a > b & a > c:
        return(f"{a} is largest")
    elif b > c:
        return(f"{b} is largest")
    else:
        return(f"{c} is largest")
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
n3 = int(input("Enter a number: ")) 
print(find_largest(n1,n2,n3))   