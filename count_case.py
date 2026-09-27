def count_case(text):
    uppercase = 0
    lowercase = 0
    digit = 0
    spaces = 0
    for ch in text:
        match ch:
            case _ if ch.isupper():
                uppercase += 1
            case _ if ch.islower():
                lowercase += 1
            case _ if ch.isdigit():
                digit += 1
            case ' ':
                spaces += 1
    return f"UpperCase: {uppercase}\nLowercase: {lowercase}\nDigits: {digit}\nSpaces: {spaces}"
print(count_case(input("Enter a sentence: ")))
   
        