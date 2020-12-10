file = open("aoc10_input.txt")
l = [0]+[int(j) for j in file.read().split("\n")]
file.close()

l = sorted(l)
l.append(max(l)+3)

print(l)

w = [0]*len(l)
w[0] = 1

for i in range(1, len(l)):
	if l[i-1] < l[i] <= l[i-1]+3:
		w[i] += w[i-1]
	if i > 0 and l[i-2] < l[i] <= l[i-2]+3:
		w[i] += w[i-2]
	if i > 1 and l[i-3] < l[i] <= l[i-3]+3:
		w[i] += w[i-3]

print(w)
print(w[len(w)-1])