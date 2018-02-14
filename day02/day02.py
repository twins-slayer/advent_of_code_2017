'part I'

with open("numbers.txt", "r") as f:
	data = f.read().strip()

checksum = 0

for line in data.split('\n'):
	num = [int(x) for x in line.split('\t')]
	checksum += max(num) - min(num)
print (checksum)