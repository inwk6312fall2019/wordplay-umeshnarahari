def is_double(word):
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i+1]:
            count = count + 1
        i = i + 2
    if count == 3:
        return True


def find_double_words():
    x = open("words.txt")
    for line in x:
        word = line.strip()
        if is_double(word):
            print(word)
