file = open("aoc6_input.txt")
l = file.read().split("\n")
file.close()

s = 0
c = [0]*26
f = True
for i in range(len(l)+1):
	if i == len(l) or l[i] == "":
		s += sum(c)
		print(c)
		c = [0]*26
		f = True
	else:
		for j in l[i]:
			if f:
				c[ord(j)-97] = 2
			else:
				c[ord(j)-97] *= 2
		f = False
	
	for j in range(len(c)):
		c[j] //= 2

print(s)