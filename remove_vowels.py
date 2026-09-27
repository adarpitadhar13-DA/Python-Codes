def remove_vowels(text):
    ch = ' '
    for i in text:
        if i not in 'AaEeIiOoUu':
            ch += i
    return ch
print(remove_vowels(input('Enter a string: ')))

