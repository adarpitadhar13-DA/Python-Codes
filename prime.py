def check_prime(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        return (f"{n} is a prime number ")
    else:
        return (f"{n} is not a prime number ")
print(check_prime(int(input("Enter a number: "))))