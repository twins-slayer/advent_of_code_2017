

with open("numbers.txt", "r") as f:
	data = f.read().strip()

result = 0
for i in range(0, len(data)):
	if data[i] == data[int(i + len(data) / 2) % len(data)]:
		result += int(data[i])
print (result)
