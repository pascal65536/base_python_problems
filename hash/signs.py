radio_eng_alphabet = {
    'a': 'alpha', 'b': 'bravo', 'c': 'charlie', 'd': 'delta',
    'e': 'echo', 'f': 'foxtrot', 'g': 'golf', 'h': 'hotel',
    'i': 'india', 'j': 'juliet', 'k': 'kilo', 'l': 'lima',
    'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa',
    'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray',
    'y': 'yankee', 'z': 'zulu'
}

words = input()
for word in words.split():
    for ch in word:
        print(radio_eng_alphabet.get(ch.lower(), ''), end=' ')
    print()
