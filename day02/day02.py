
'part I'

with open("numbers.txt", "r") as f:
	checksum = 0

	for line in f:
		num = [int(x) for x in line.split('\t')]
		checksum += max(num) - min(num)
	print (checksum)

'part II'

with open("numbers.txt", "r") as f:

	result = 0
	for line in f:
		num = [int(x) for x in line.split('\t')]
		for a in num:
			for b in num:
				if a != b and a % b == 0:
					result += a / b
	print (result)
	

