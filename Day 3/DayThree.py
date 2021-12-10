# Read content of input file
def read_file(file_name):
	with open(file_name, 'r') as file:
		return file.read()

def find_most_common_bit_per_position(power_consumption):
	gamma = {}
	key = 0

	for bit in power_consumption[0]:
		gamma[key] = {0: 0, 1: 0}

		key+=1

	for bit in power_consumption:
		for i in range(len(bit)):
			gamma[i][int(bit[i])] += 1

	return gamma

def create_binary_gamma(most_common_bit_per_position):
	binary_gamma = ''

	for i in range(len(most_common_bit_per_position)):
		if most_common_bit_per_position[i][0] > most_common_bit_per_position[i][1]:
			binary_gamma += '0'
		else:
			binary_gamma += '1'

	return binary_gamma

# invert binary string 
def invert_binary(binary):
	new_binary = ''
	for i in range(len(binary)):
		if binary[i] == '0':
			new_binary += '1'
		else:
			new_binary += '0'

	return new_binary

# convert binary string to decimal
def binary_to_decimal(binary):
	return int(binary, 2)

def filter_oxygen_binary(power_consumption, most_common_bit_per_position, position = 0):
	if len(power_consumption) < 2:
		return power_consumption

	filtered_power_consumption = []
	most_common_bit = 0 if most_common_bit_per_position[position][0] > most_common_bit_per_position[position][1] else 1

	for i in range(len(power_consumption)):
		if power_consumption[i][position] == str(most_common_bit):
			filtered_power_consumption.append(power_consumption[i])

	if len(filtered_power_consumption) == 0:
		filtered_power_consumption = power_consumption

	if position == len(power_consumption[0])-1:
		return filtered_power_consumption

	most_common_bit_per_position = find_most_common_bit_per_position(filtered_power_consumption)

	return filter_oxygen_binary(filtered_power_consumption, most_common_bit_per_position, position + 1)

def filter_co2_binary(power_consumption, most_common_bit_per_position, position = 0):
	if len(power_consumption) < 2:
		return power_consumption

	filtered_power_consumption = []
	least_common_bit = 0 if most_common_bit_per_position[position][0] <= most_common_bit_per_position[position][1] else 1

	for i in range(len(power_consumption)):
		if power_consumption[i][position] == str(least_common_bit):
			filtered_power_consumption.append(power_consumption[i])
		
	if len(filtered_power_consumption) == 0:
		filtered_power_consumption = power_consumption

	if position == len(power_consumption[0])-1:
		return filtered_power_consumption

	most_common_bit_per_position = find_most_common_bit_per_position(filtered_power_consumption)

	return filter_co2_binary(filtered_power_consumption, most_common_bit_per_position, position + 1)





input = read_file('input.txt')

power_consumption = input.split('\n')

most_common_bit_per_position = find_most_common_bit_per_position(power_consumption)
gamma = create_binary_gamma(most_common_bit_per_position)
decimal_gamma = binary_to_decimal(str(gamma))

epsilon = invert_binary(gamma)
decimal_epsilon = binary_to_decimal(str(epsilon))

oxygen = filter_oxygen_binary(power_consumption, most_common_bit_per_position)
oxygen_decimal = binary_to_decimal(str(oxygen[0]))

co2 = filter_co2_binary(power_consumption, most_common_bit_per_position)
co2_decimal = binary_to_decimal(str(co2[0]))

print(oxygen_decimal, co2_decimal, co2_decimal * oxygen_decimal)