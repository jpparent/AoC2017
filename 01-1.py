f = open('01-1.input')
inputs = f.read()
f.close()

sum = 0

matches = []

last = 0
for i in inputs:
	if i == last:
		matches.append(i)
	last = i

#loop for the last one
if i == inputs[0]:
	matches.append(i)

for p in matches:
	sum = sum + int(p)

print(sum)