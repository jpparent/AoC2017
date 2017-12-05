f = open('05-1.input')
rows = f.readlines()
f.close()

steps = 0

jumps = [int(x) for x in rows]
j = 0
while (j >= 0 and j < len(jumps)): 
	prevJ = j
	j += jumps[j]

	steps += 1
	if jumps[prevJ] >= 3:
		jumps[prevJ] -= 1
	else:
		jumps[prevJ] += 1

print(steps)