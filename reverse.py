def reverse_number(n):
    rem = 1
    sum = 0
    while n > 0:
        rem = n % 10
        sum = sum*10 + rem
        n = n // 10
    return sum
print(reverse_number(int(input("Enter a number: "))))

