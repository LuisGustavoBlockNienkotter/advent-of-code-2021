# Read content of input file
def read_file(file_name):
	with open(file_name, 'r') as file:
		return file.read()

# count the number of times that the depth increases
def count_increases(depths):
	count = 0
	for i in range(1, len(depths)):
		if int(depths[i]) > int(depths[i-1]):
			count += 1
	return count

# separate the depths into chunks of three
def chunk_depths(depths):
	chunks = []
	for i in range(0, len(depths)):
		#check if the chunck is smaller than 3
		if i + 3 <= len(depths):
			chunks.append(depths[i:i+3])
	return chunks

# sum the depths of the chunks and return an array with the sums
def sum_chunks(chunks):
	sums = []
	for chunk in chunks:
		total = 0
		for depth in chunk:
			total += int(depth)

		sums.append(total)
	return sums

input = read_file('input.txt')

# create a list of all the words in the input
depths = input.split()

chunks = chunk_depths(depths)
sums_chunks = sum_chunks(chunks)

count_increases = count_increases(sums_chunks);

print(count_increases)
