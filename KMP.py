def kmpPre(x):
	b = [0] * (len(x) + 1)
	b[0] = j = -1
	for i in range(1, len(x) + 1):
		while j >= 0 and x[j] != x[i - 1]:
			j = b[j]
		j += 1
		b[i] = j
	return b

def kmpSearch(s, x):
	b = kmpPre(x)
	j = -1
	for i in range(1, len(s) + 1):
		while j >= 0 and x[j] != s[i - 1]:
			j = b[j]
		j += 1
		if j == len(x):
			print("match encontrado en", i - len(x))
			j = b[j]
