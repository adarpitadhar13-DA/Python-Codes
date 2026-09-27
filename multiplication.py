def multiplication_table(n):
    for i in range(0,11):
        print(f"{n} * {i} = {i*n}")

multiplication_table(int(input("Enter a number: ")))
