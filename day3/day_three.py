import sys
sys.setrecursionlimit(3000000)

def part_one(file):
	input = open(file, 'r')
	Lines = input.readlines()
	readout_sums = get_readout_sums(Lines)

	gamma = [0] * len(readout_sums)
	epsilon = [0] * len(readout_sums)

	bit_count = 0
	for bit_sum in readout_sums:
		if bit_sum >= 500:
			gamma[bit_count] = 1
		elif bit_sum < 500:
			epsilon[bit_count] = 1
		bit_count += 1

	return int(tostring(gamma), 2) * int(tostring(epsilon), 2)

def part_two(file):
	input = open(file, 'r')
	Lines = input.readlines()

	search_space = convert_lines_to_lists(Lines)

	count = 0

	o2_result = int(tostring(popularity_contest(search_space, count, "o2")[0]), 2)
	co2_result = int(tostring(popularity_contest(search_space, count, "co2")[0]), 2)

	return o2_result * co2_result

def popularity_contest(search_space, index, gas):
	bit_sum = 0
	new_search_space = []
	for line in search_space:
		bit_sum += int(line[index])
	if gas == "o2":
		if float(bit_sum) >= len(search_space)/2:
			popular = 1
		else:
			popular = 0
	elif gas == "co2":
		if float(bit_sum) >= len(search_space)/2:
			popular = 0
		else:
			popular = 1
	for line in search_space:
		if int(line[index]) == popular:
			new_search_space.append(line)
	if(len(new_search_space) > 1):
		return popularity_contest(new_search_space, index + 1, gas)
	else:
		return new_search_space

	
def filter(binary, bit, criteria):
	keep = []
	for item in binary:
		if int(item[bit]) == criteria:
			keep.append(item)
	if(len(keep) == 0):
		return binary
	return keep


def tostring(array):
	result = ""
	for element in array:
		result = result + str(element)
	return result

def convert_lines_to_lists(Lines):
	result = []
	for line in Lines:
		readout = list(line.strip())
		result.append(readout)
	return result

def get_readout_sums(Lines):
	readout_sums = []

	for line in Lines:
		readout = list(line.strip())
		if len(readout_sums) != len(readout):
			readout_sums = [0] * len(readout)
		bit_count = 0
		for bit in readout:
			readout_sums[bit_count] += int(bit)
			bit_count +=1
	return readout_sums

if __name__ == '__main__':
	print(part_one('input.txt'))
	print(part_two('input.txt'))