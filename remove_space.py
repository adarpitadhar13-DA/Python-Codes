def remove_spaces(text):
    result = ' '
    for ch in text:
        if ch != ' ':
            result += ch
    return result
Sentence = input("Enter a sentence: ")
print(remove_spaces(Sentence))