def count_vowels_consonants(text):
    count1 = 0
    count2 = 0
    for ch in text:
        if ch in 'AaEeIiOoUu':    
            count1 += 1
        else:
            count2 += 1
    return f"Vowels = {count1},\nConsonants = {count2}"
String = print(count_vowels_consonants(input("Enter a string: ")))


