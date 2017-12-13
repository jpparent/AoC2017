f = open('12.input')
input = f.readlines()
f.close()

register = {}

for line in input:
	id = line[:line.index('<')-1]
	links = line[line.index('>')+1:].strip()
	register[id] = links.split(', ')

groups = set([])

def recursiveAdd(key):
	if key not in register:
		return
	if key in groups:
		return

	if key not in groups:
		groups.add(key)

	for x in register[key]:
		recursiveAdd(x)

	# this is pretty hackish...
	# remove the elements that are part of a group
	# and count each time we restart the recursive add
	# which will start on an element that is naturaly 
	# part of a different group
	del register[key]

numGroups = 0
while len(register) > 0:

	recursiveAdd(list(register)[0])
	numGroups += 1
	

print(numGroups)