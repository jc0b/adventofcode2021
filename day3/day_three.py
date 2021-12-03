import sys
sys.setrecursionlimit(3000000)

def part_one():
	input = open('input.txt', 'r')
	Lines = input.readlines()
 
	horizontal = 0
	vertical = 0
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

def part_two():
	input = open('input.txt', 'r')
	Lines = input.readlines()
	readout_sums = get_readout_sums(Lines)
	#print(readout_sums)

	oxygen_search_string = [0] * len(readout_sums)
	co2_search_string = [0] * len(readout_sums)

	bit_count = 0
	for bit_sum in readout_sums:
		if bit_sum >= 500:
			oxygen_search_string[bit_count] = 1
		elif bit_sum < 500:
			co2_search_string[bit_count] = 1
		bit_count += 1

	print(f"Search: {tostring(oxygen_search_string)}")

	search_space = convert_lines_to_lists(Lines)
	bit_index = 0
	for bit in oxygen_search_string:
		search_space = filter(search_space, bit_index, bit)
		bit_index +=1
	print(f"Result: {tostring(search_space[0])}")
	o2_result = int(tostring(search_space[0]), 2)

	print(f"Search: {tostring(co2_search_string)}")
	search_space = convert_lines_to_lists(Lines)
	bit_index = 0
	for bit in co2_search_string:
		search_space = filter(search_space, bit_index, bit)
		bit_index +=1
	print(f"Result: {tostring(search_space[0])}")
	co2_result = int(tostring(search_space[0]), 2)

	print(o2_result)
	print(co2_result)
	return o2_result * co2_result

	
def filter(binary, bit, criteria):
	keep = []
	for item in binary:
		#print(f"Criteria = {criteria}")
		#print(f"{item[bit]=}")
		if int(item[bit]) == criteria:
			#print(f"{item}, {bit}")
			keep.append(item)
	if(len(keep) == 0):
		return binary
	return keep





def match_recurse(o2_string, co2_string, Lines):
	for line in Lines:
		if co2_string == line.strip():
			print(f"Found a match: {co2_string}")
		elif o2_string == line.strip():
			print(f"Found a match: {o2_string}")
		else:
			match_recurse(o2_string[:-1], co2_string[:-1], Lines)


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
	print(part_one())
	print(part_two())