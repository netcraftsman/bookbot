with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    #print(file_contents)
    words = len(file_contents.split())
    fbook = file_contents.lower()
    chars = {}
    count = 0
    val = 0
    letters_list = []
    
    
    for word in fbook:
        for letter in word:
            letters_list += letter
            chars[letter] = val

    letters_set = set(letters_list)
    for char, val in chars.items():
        for letter in letters_list:
            if char == letter:
                val += 1
                chars[letter] = val

    letters_list = list(letters_set)
    for char, val in chars.items():
        if char.upper() != char:

            print(f"The '{char}' character was found, {val} times")