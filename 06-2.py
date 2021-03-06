input = "11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11"

banks = [int(x) for x in input.split()]
snapshots = set()
snapshots.add(str(banks))

lenBanks = len(banks)

loopSize = 0
loopStarted = False
snapshotToRemember = ""

toDistribute = 0
i = 0
while True:
	i = banks.index(max(banks))

	toDistribute = int(banks[i])
	banks[i] = 0
	
	while toDistribute > 0:
		i += 1
		if i == lenBanks:
			i = 0
		banks[i] += 1
		toDistribute -= 1

	snapshot = str(banks)

	if snapshot in snapshots and not loopStarted:
		snapshotToRemember = snapshot
		loopStarted = True
		continue

	if loopStarted:
		loopSize += 1

	if snapshot == snapshotToRemember:
		break # we're done here

	snapshots.add(str(banks))

print(loopSize)