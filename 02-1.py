f = open('02-1.input')
rows = f.readlines()
f.close()

checksum = 0

for row in rows:
	values = [int(x) for x in row.split()]
	checksum += max(values) - min(values)

print(checksum)