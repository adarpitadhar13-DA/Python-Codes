def count_consonants(text):
    count = 0
    for ch in text:
        if ch not in 'AaEeIiOoUu':    
            count += 1
    return (f"The number of consonants are {count}")
print(count_consonants(input("Enter a string: ")))
