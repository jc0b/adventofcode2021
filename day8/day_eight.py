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

	
if __name__ == '__main__':
	print(part_one('input.txt'))
	print(part_two('input.txt'))