


# Read content of input file
def read_file(file_name):
	with open(file_name, 'r') as file:
		return file.read()

# separate commands on space
def separate_commands(commands):
	forward = 0
	depth = 0
	aim = 0

	for command in commands:
		command = command.split(' ')
		
		if command[0] == 'forward':
			forward += int(command[1])
			depth += aim * int(command[1])

		if command[0] == 'up':
			aim -= int(command[1])

		if command[0] == 'down':
			aim += int(command[1])

	return forward, depth

input = read_file('input.txt')

# #separate input in lines
commands = input.split('\n')
forward, depth = separate_commands(commands)

print(forward, depth, forward * depth)