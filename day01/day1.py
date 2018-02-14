"Part I"

with open("numbers.txt", "r") as f:
	data = f.read().strip()

data += data[0]
result = 0
for i in range(0, len(data) - 1):
	if data[i] == data[i + 1]:
		result += int(data[i])
print (result)


"Part II"

with open("numbers.txt", "r") as f:
	data = f.read().strip()

result = 0
for i in range(0, len(data)):
	if data[i] == data[int(i + len(data) / 2) % len(data)]:
		result += int(data[i])
print (result)