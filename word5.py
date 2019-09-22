def uses_all(word, req_letters):
    for letter in req_letters:
        if letter not in word:
            return False
    return True
