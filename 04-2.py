f = open('04-1.input')
rows = f.readlines()
f.close()

sum = 0

for row in rows:
	words = row.split()

	for i in range(0,len(words)):
		words[i] = ''.join(sorted(words[i]))
	
	origLen = len(words)
	uniqueLen = len(set(words))

	if uniqueLen == origLen:
		sum += 1	

print(sum)