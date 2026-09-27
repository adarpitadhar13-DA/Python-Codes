def count_vowels(text):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for ch in text.lower():
        if ch == 'a':
            a += 1
        elif ch == 'e':
            e += 1
        elif ch == 'i':
            i += 1
        elif ch == 'o':
            o += 1
        elif ch == 'u':
            u += 1
    print(f"a = {a}")
    print(f"e = {e}")
    print(f"i = {i}")
    print(f"o = {o}")
    print(f"u = {u}")
count_vowels(input("Enter a string: "))