def char():
	x=open("words.txt")
	for line in x:
	words=line.strip()
	if len(words)>20:
		print (words)
char()
