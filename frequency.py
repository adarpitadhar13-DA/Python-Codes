def character_frequency(text, ch):
    count = 0
    text = text.lower()
    ch = ch.lower()
    for i in text:
        if ch == i:
            count += 1
    return f"Frequency of {ch} is {count}"
sentence =  input("Enter a Sentence: ")
letter = input("Enter a character: ")
print(character_frequency(sentence, letter))
