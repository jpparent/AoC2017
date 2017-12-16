f = open('16.input')
moves = f.read()
f.close()
moves = moves.split(',')

progs = "abcdefghijklmnop"
initProgs = "abcdefghijklmnop"

def justDance():
	global progs
	global moves
	
	for move in moves:
		if move[0] == 's':
			spinX = int(move[1:])
			progs = progs[-spinX::] + progs[:-spinX]

		if move[0] == 'x':
			iA, iB = [int(x) for x in move[1:].split('/')]
			lsProgs = list(progs)
			lsProgs[iA] = progs[iB]
			lsProgs[iB] = progs[iA]
			progs = ''.join(lsProgs)

		if move[0] == 'p':
			iA, iB = [progs.index(x) for x in move[1:].split('/')]
			lsProgs = list(progs)
			lsProgs[iA] = progs[iB]
			lsProgs[iB] = progs[iA]
			progs = ''.join(lsProgs)

# first, find out what is your cycle length
# to do so, perform the dance loop until you
# get the initial order again

i = 0
while progs != initProgs or i == 0:

	justDance()
	i+=1

cycleLength = i

# then you need to know how many more dance loops
# you need to do to get to the billionth one

remainingLoops = 1000000000 % cycleLength

# then you just need to perform the remaining loops
for i in range(0, remainingLoops):

	justDance()
	
print(progs)