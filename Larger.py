def find_largest(a,b):
    if a> b:
        return(f"{a} is Larger")
    else:
        return(f"{b} is larger")
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
print(find_largest(n1,n2))
