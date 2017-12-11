f = open('09-1.input')
input = f.read()
f.close()

# remove garbage
while '!' in input:
	i = input.index('!')
	input = input[:i] + input[i+2:]

while '<' in input:
	start = input.index('<')
	end = input.index('>')
	input = input[:start] + input[end + 1:]

input = input.replace(',','')

sum = 0
level = 1
last = ""
for x in input:
	if x == '{' and last == '{':
		level += 1
	if x == '}':
		if last == '}':
			level -= 1
		sum += level

	last = x

print(sum)