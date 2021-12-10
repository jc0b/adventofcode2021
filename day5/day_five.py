import re

# (\d+,\d+)\s->\s(\d+,\d+)

def part_one(file):
	input = open(file, 'r')
	Lines = input.readlines()

	vectors = []
	grid = [[0 for c in range(999)] for r in range(999)]

	for line in Lines:
		(re.match("(\d+,\d+)\s->\s(\d+,\d+)", line.strip()).groups()[0].split(), re.match("(\d+,\d+)\s->\s(\d+,\d+)", line.strip()).groups()[1].split())
		vectors.append((re.match("(\d+,\d+)\s->\s(\d+,\d+)", line.strip()).groups()[0].split(","), re.match("(\d+,\d+)\s->\s(\d+,\d+)", line.strip()).groups()[1].split(",")))
	# print(vectors[0])
	count = 0
	for vector in vectors:
		if vector[0][0] == vector[1][0]:
			# vertical line
			# print(f"V: {vector}")
			if int(vector[0][1]) - int(vector[1][1]) <= 0:
				# range is ascending
				for i in range(int(vector[0][1]), int(vector[1][1])+1):
					x = int(vector[0][0])
					#print(len(grid))
					grid[x][i] +=1
			elif int(vector[0][1]) - int(vector[1][1]) > 0:
				# range is descending
				for i in range(int(vector[0][1]), int(vector[1][1])-1, -1):
					x = int(vector[0][0])
					#print(len(grid))
					grid[x][i] +=1
				
		elif vector[0][1] == vector[1][1]:
			# horizontal line
			# print(f"H: {vector}")
			if int(vector[0][0]) - int(vector[1][0]) <= 0:
				# range is ltr
				y = int(vector[0][1])
				for i in range(int(vector[0][0]), int(vector[1][0])+1):
					#print(len(grid))
					grid[i][y] +=1
			if int(vector[0][0]) - int(vector[1][0]) > 0:
				# range is rtl
				y = int(vector[0][1])
				for i in range(int(vector[0][0]), int(vector[1][0])-1, -1):
					#print(len(grid))
					grid[i][y] +=1
	# printgrid(grid)
	intersections = 0
	for i, x in enumerate(grid):
		for j, y in enumerate(grid[i]):
			if grid[i][j] > 1:
				intersections +=1
	return intersections

def part_two(file):
	input = open(file, 'r')
	Lines = input.readlines()

	vectors = []
	grid = [[0 for c in range(999)] for r in range(999)]

	for line in Lines:
		(re.match("(\d+,\d+)\s->\s(\d+,\d+)", line.strip()).groups()[0].split(), re.match("(\d+,\d+)\s->\s(\d+,\d+)", line.strip()).groups()[1].split())
		vectors.append((re.match("(\d+,\d+)\s->\s(\d+,\d+)", line.strip()).groups()[0].split(","), re.match("(\d+,\d+)\s->\s(\d+,\d+)", line.strip()).groups()[1].split(",")))
	# print(vectors[0])
	count = 0
	for vector in vectors:
		if vector[0][0] == vector[1][0]:
			# vertical line
			# print(f"V: {vector}")
			if int(vector[0][1]) - int(vector[1][1]) <= 0:
				# range is ascending
				for i in range(int(vector[0][1]), int(vector[1][1])+1):
					x = int(vector[0][0])
					#print(len(grid))
					grid[x][i] +=1
			elif int(vector[0][1]) - int(vector[1][1]) > 0:
				# range is descending
				for i in range(int(vector[0][1]), int(vector[1][1])-1, -1):
					x = int(vector[0][0])
					#print(len(grid))
					grid[x][i] +=1
				
		elif vector[0][1] == vector[1][1]:
			# horizontal line
			# print(f"H: {vector}")
			if int(vector[0][0]) - int(vector[1][0]) <= 0:
				# range is ltr
				y = int(vector[0][1])
				for i in range(int(vector[0][0]), int(vector[1][0])+1):
					#print(len(grid))
					grid[i][y] +=1
			if int(vector[0][0]) - int(vector[1][0]) > 0:
				# range is rtl
				y = int(vector[0][1])
				for i in range(int(vector[0][0]), int(vector[1][0])-1, -1):
					#print(len(grid))
					grid[i][y] +=1
		else:
			# diagonal line
			# print(f"D: {vector}")

			## 797,795 -> 273,271
			## 797 > 273 && 795 > 271 -> \ rtl
			## 105,945 -> 972,78
			## 105 < 972 && 945 > 78 -> / ltr
			## 511,332 -> 19,824
			## 511 > 19 && 332 < 824 -> / rtl

			if int(vector[0][0]) > int(vector[1][0]):
				# if x1 > x2 
				if int(vector[0][1]) > int(vector[1][1]):
					# if y1 > y2
					# \ rtl
					# decrease x
					# decrease y
					x = int(vector[0][0])
					y = int(vector[0][1])
					while x >= int(vector[1][0]) and y >= int(vector[1][1]):
						grid[x][y] += 1
						x -= 1
						y -= 1
				if int(vector[0][1]) < int(vector[1][1]):
					# if y1 < y2
					# / rtl
					# decrease x
					# increase y
					x = int(vector[0][0])
					y = int(vector[0][1])
					while x >= int(vector[1][0]) and y <= int(vector[1][1]):
						grid[x][y] += 1
						x -= 1
						y += 1

			if int(vector[0][0]) < int(vector[1][0]):
				# if x1 < x2
				if int(vector[0][1]) > int(vector[1][1]):
					# if y1 > y2
					# / ltr
					# increase x
					# decrease y
					x = int(vector[0][0])
					y = int(vector[0][1])
					while x <= int(vector[1][0]) and y >= int(vector[1][1]):
						grid[x][y] += 1
						x += 1
						y -= 1
				if int(vector[0][1]) < int(vector[1][1]):
					# if y1 < y2
					# \ ltr
					# increase x
					# increase y
					x = int(vector[0][0])
					y = int(vector[0][1])
					while x <= int(vector[1][0]) and y <= int(vector[1][1]):
						grid[x][y] += 1
						x += 1
						y += 1
	# printgrid(grid)
	intersections = 0
	for i, x in enumerate(grid):
		for j, y in enumerate(grid[i]):
			if grid[i][j] > 1:
				intersections +=1
	return intersections


def printgrid(grid):
	for row in grid:
		print(row)

if __name__ == '__main__':
	print(part_one('input.txt'))
	print(part_two('input.txt'))