f = open('09-1.input')
input = f.read()
f.close()

# remove escaped characters
while '!' in input:
	i = input.index('!')
	input = input[:i] + input[i+2:]

gargabeSize = 0
while '<' in input:
	start = input.index('<')
	end = input.index('>')
	input = input[:start] + input[end + 1:]
	gargabeSize += (end - start) -1

print(gargabeSize)