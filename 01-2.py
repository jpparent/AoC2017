f = open('01-1.input')
inputs = f.read()
f.close()

sum = 0
length = len(inputs)
halfLength = length//2

matches = []

compare = 0
for i in range(0, length):
	current = inputs[i]
	compare = inputs[(i + halfLength) % length]
	
	if current == compare:
		matches.append(current)

for p in matches:
	sum = sum + int(p)

print(sum)