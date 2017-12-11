f = open('11.input')
input = f.read().strip()
f.close()

steps = input.split(',')

posX = posY = 0
furthest = 0

def distance(x,y):
	x = abs(x)
	y = abs(y)
	return x + max(0, (y-x)//2)

# move
for step in steps:
	if step == 'n':
		posY += 2
	if step == 'ne':
		posX += 1
		posY += 1
	if step == 'se':
		posX += 1
		posY += -1
	if step == 's':
		posY += -2
	if step == 'sw':
		posX += -1
		posY += -1
	if step == 'nw':
		posX += -1
		posY += 1
	
	dist = distance(posX,posY)
	if dist > furthest:
		furthest = dist


print(furthest)
