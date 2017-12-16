f = open('16.input')
moves = f.read()
f.close()
moves = moves.split(',')

progs = "abcdefghijklmnop"

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

print(progs)
