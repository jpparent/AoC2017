import math
input = 277678

root = math.sqrt(input)
highestRootInLayer = int(root) +1
# the roots are always odd numbers
if highestRootInLayer % 2 == 0:
	highestRootInLayer += 1

highestInLayer = highestRootInLayer * highestRootInLayer

diff = highestInLayer - input

# the manathan distance from a corner is of (highestRoot -1)
distance = (highestRootInLayer - 1) - diff 
 
print(distance)