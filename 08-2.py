f = open('08-1.input')
lines = f.readlines()
f.close()

register = {}
historicalMax = 0

for line in lines:
	arrStr = line.split()
	name = arrStr[0]
	inc = int(arrStr[2])
	if arrStr[1] == "dec":
		inc *= -1
	condKey = arrStr[4]
	condOp = arrStr[5]
	condVal = int(arrStr[6])

	if name not in register:
		register[name] = 0
	if condKey not in register:
		register[condKey] = 0

	#check condition
	if eval("register[condKey]" + condOp + str(condVal)) == True:
		register[name] += inc

	if register[name] > historicalMax:
		historicalMax = register[name]

	
print( max(register.values()) )
print( historicalMax )