def part_one(file):
	input = open(file, 'r')
	Lines = input.readlines()

	lanternfish_school = [int(x) for x in Lines[0].strip().split(",")]
	for i in range(80):
		new_fish = []
		for i, fish in enumerate(lanternfish_school):
			if lanternfish_school[i] == 0:
				new_fish.append(8)
				lanternfish_school[i] = 6
				continue
			lanternfish_school[i] -= 1
		lanternfish_school += new_fish

	return len(lanternfish_school)

def part_two(file):
	input = open(file, 'r')
	Lines = input.readlines()

	lanternfish_school = [int(x) for x in Lines[0].strip().split(",")]

	lanternfish_buckets = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}
	for fish in lanternfish_school:
		if fish == 0:
			lanternfish_buckets["0"] +=1
		elif fish == 1:
			lanternfish_buckets["1"] +=1
		elif fish == 2:
			lanternfish_buckets["2"] +=1
		elif fish == 3:
			lanternfish_buckets["3"] +=1
		elif fish == 4:
			lanternfish_buckets["4"] +=1
		elif fish == 5:
			lanternfish_buckets["5"] +=1
		elif fish == 6:
			lanternfish_buckets["6"] +=1
		elif fish == 7:
			lanternfish_buckets["7"] +=1
		elif fish == 8:
			lanternfish_buckets["8"] +=1
	
	for i in range(256):
		new_fish_this_round = 0
		if lanternfish_buckets["0"] > 0:
			new_fish_this_round = lanternfish_buckets["0"]
			lanternfish_buckets["0"] = 0

		lanternfish_buckets["0"] = lanternfish_buckets["1"]
		lanternfish_buckets["1"] = lanternfish_buckets["2"]
		lanternfish_buckets["2"] = lanternfish_buckets["3"]
		lanternfish_buckets["3"] = lanternfish_buckets["4"]
		lanternfish_buckets["4"] = lanternfish_buckets["5"]
		lanternfish_buckets["5"] = lanternfish_buckets["6"]
		lanternfish_buckets["6"] = lanternfish_buckets["7"] + new_fish_this_round
		lanternfish_buckets["7"] = lanternfish_buckets["8"]
		lanternfish_buckets["8"] = new_fish_this_round

	population = 0
	for key in lanternfish_buckets:
		population += lanternfish_buckets[key]
	return population

if __name__ == '__main__':
	print(part_one('input.txt'))
	print(part_two('input.txt'))