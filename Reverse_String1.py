def reverse_string(text):
    reverse = ''
    for ch in text:
        reverse = ch + reverse
    return f"Reverse of this string: {reverse}"
print(reverse_string(input("Enter a string: ")))
