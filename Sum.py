def sum_natural(n):
    add = 0
    for i in range(n+1):
        add += i
    return add
number=int(input("Enter a number: "))
print(sum_natural(number))