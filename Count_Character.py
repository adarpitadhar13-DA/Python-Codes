def count_characters(text):
    count = 0
    for i in text:
        count += 1
    return (f"The number of characters are {count}")
print(count_characters(input("Enter a string: ")))