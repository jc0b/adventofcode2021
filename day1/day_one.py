def part_one(file):
	input = open(file, 'r')
	Lines = input.readlines()
 
	higher = 0
	prev = 0
	line_number = 0

	for line in Lines:
		current = line.strip()
		if line_number != 0 and prev < int(current):
			higher +=1
		
		prev = int(current)
		line_number += 1
	return(higher)

def part_two(file):
	input = open(file, 'r')
	Lines = input.readlines()
 
	numbers = []

	for line in Lines:
		numbers.append(int(line.strip()))

	higher = 0
	index = 0
	prev = 0
	for number in numbers:
		if (index + 1) < (len(numbers) - 1):
			total = numbers[index] + numbers[index+1] + numbers[index+2]

			if index != 0 and prev < total:
					higher +=1
				
			prev = total
			index += 1
	return higher

if __name__ == '__main__':
	print(part_one('input.txt'))
	print(part_two('input.txt'))