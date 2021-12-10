def part_one(file):
	input = open(file, 'r')
	Lines = input.readlines()

	crab_horizontal = [int(x) for x in Lines[0].strip().split(",")]
	max_crab = max(crab_horizontal)
	smallest_sum = 10000000000000
	for i in range(0, max_crab):
		movement_sum = 0
		for j in crab_horizontal:
			movement_sum += abs(j - i)
		if movement_sum < smallest_sum:
			smallest_sum = movement_sum
	return smallest_sum

def part_two(file):
	input = open(file, 'r')
	Lines = input.readlines()

	crab_horizontal = [int(x) for x in Lines[0].strip().split(",")]
	max_crab = max(crab_horizontal)
	smallest_sum = 10000000000000
	for i in range(0, max_crab):
		movement_sum = 0
		for j in crab_horizontal:
			movement_sum += (abs(j - i) + 1) * abs(j - i) * 0.5
		if movement_sum < smallest_sum:
			smallest_sum = movement_sum
	return int(smallest_sum)

if __name__ == '__main__':
	print(part_one('input.txt'))
	print(part_two('input.txt'))


## for every possible movement value
## 