def part_one(file):
	input = open(file, 'r')
	Lines = input.readlines()
	count = 0
	for line in Lines:
		for i in line.strip().split("|")[1].split():
			if len(i) == 2 or len(i) == 4 or len(i) == 3 or len(i) == 7:
				count += 1
	return count


	

def part_two(file):
	input = open(file, 'r')
	Lines = input.readlines()

	results = []
	for line in Lines:
		lhs = line.strip().split("|")[0].split()
		result = ""
		dic = {}
		for i in lhs:
			if len(i) == 2:
				dic[1] = i
			elif len(i) == 4:
				dic[4] = i
			elif len(i) == 3:
				dic[7] = i
			elif len(i) == 7:
				dic[8] = i
		for i in lhs:
			if len(i) == 5:
				if not (set(dic[7]) - set(i)):
					dic[3] = i
				elif not ((set(dic[4])-set(dic[7])) - set(i)):
					dic[5] = i
				else:
					dic[2] = i
			elif len(i) == 6:
				if not (set(dic[4]) - set(i)):
					dic[9] = i
				elif not ((set(dic[4])-set(dic[7])) - set(i)):
					dic[6] = i
				else:
					dic[0] = i
			# read output
		rhs = line.strip().split("|")[1].split()
		for m in rhs:
			for key, val in dic.items():
				if set(val) == set(m):
					result += str(key)
					break
		results.append(result)
	# print(outputs)
	return sum([int(x) for x in results])

	
if __name__ == '__main__':
	print(part_one('input.txt'))
	print(part_two('input.txt'))