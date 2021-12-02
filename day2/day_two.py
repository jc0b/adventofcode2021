
def part_one():
	input = open('input.txt', 'r')
	Lines = input.readlines()
 
	horizontal = 0
	vertical = 0

	for line in Lines:
		instructions = line.strip().split()
		result = parse_instructions(instructions)
		horizontal += result[0]
		vertical += result[1]
	return(horizontal*vertical)

def part_two():
	input = open('input.txt', 'r')
	Lines = input.readlines()
 
	horizontal = 0
	vertical = 0
	aim = 0

	for line in Lines:
		instructions = line.strip().split()
		result = parse_instructions(instructions)
		aim += result[1]
		horizontal += result[0]
		vertical += result[0] * aim
			
	return(horizontal*vertical)

def parse_instructions(instructions):
	instructions[1] = int(instructions[1])
	if instructions[0] == "forward":
		return (instructions[1], 0)
	elif instructions[0] == "up":
		return (0, -instructions[1])
	elif instructions [0] == "down":
		return (0, instructions[1])

if __name__ == '__main__':
	print(part_one())
	print(part_two())