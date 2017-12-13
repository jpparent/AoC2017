f = open('12.input')
input = f.readlines()
f.close()

register = {}

for line in input:
	id = line[:line.index('<')-1]
	links = line[line.index('>')+1:].strip()
	register[id] = links.split(', ')

id0groups = set([])

def recursiveAdd(key):
	if key not in register:
		return
	if key in id0groups:
		return

	if key not in id0groups:
		id0groups.add(key)

	for x in register[key]:
		recursiveAdd(x)

recursiveAdd('0')

print(len(id0groups))