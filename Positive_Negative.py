def check_number(n):
    if n > 0:
        print(f"{n} is Positive Number")
    elif n < 0:
        print(f"{n} is Negative Number")
    else:
        print(f"the number is 0")
check_number(int(input("Enter a number: ")))