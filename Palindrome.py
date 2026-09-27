def check_palindrome(text):
    original = text
    text = text.lower()
    reverse = ''

    for ch in text:
        reverse = ch + reverse

    if reverse == text:
        return f"{original} is Palindrome"
    else:
        return f"{original} is not Palindrome"


print(check_palindrome(input("Enter a string: ")))