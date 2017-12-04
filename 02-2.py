f = open('02-1.input')
rows = f.readlines()
f.close()

sum = 0

for row in rows:
	values = [int(x) for x in row.split()]
	
	for i in range(0,len(values)):
		current = values[i]
		for j in range(0, len(values)):
			if i != j and current % values[j] == 0:
				sum += current / values[j]

print(sum)