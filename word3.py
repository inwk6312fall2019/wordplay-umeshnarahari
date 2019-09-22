x = open('words.txt')

def avoids(word,string):
    for char in word:
        if char in letter:
            return False
    return True


letter = raw_input('What letters to exclude? ')
count = 0
for line in x:
    word = line.strip()
    if avoids(word, string):
        count += 1
        print word

percent = (count / 113809.0) * 100

print str(percent) + "% of the words don't have " + letter + '.'
