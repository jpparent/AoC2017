f = open('04-1.input')
rows = f.readlines()
f.close()

sum = 0

for row in rows:
	words = row.split()
	origLen = len(words)

	uniqueLen = len(set(words))

	if uniqueLen == origLen:
		sum += 1	

print(sum)