def count_vowels(text):
    count = 0
    for ch in text:
        if ch in 'AaEeIiOoUu':    
            count += 1
    return (f"The number of vowels are {count}")
print(count_vowels(input("Enter a string: ")))
