
def file_input(filepath):
	f = open(filepath)
	global commands 
	commands = f.read()
	f.close()

def execute(char, iteration = -1):	#implemet a limit at execution cycles
	data = []
	output = []
	data_index = 0
	command_index = 0
	stopper=0
	global commands
	while command_index < len(commands):
		stopper += 1
		i = commands[command_index]
		if len(data) == data_index:
			data.append(0)
		if i == '>':
			data_index += 1
		elif i == '<':
			if data_index == 0:
				data = [0] + data
			else:
				data_index -= 1
		elif i == '+':
			data[data_index] += 1
		elif i == '-':
			data[data_index] -=  1
		elif i == '.':
			if char:
				output.append(chr(data[data_index]))
			else:
				output.append(data[data_index])
		elif i == ',':
			while True:
				a = int(input ('Insert the datum at position ' + str(data_index+1) + ': '))
				if (type(a) is int):
					data[data_index] = a
					break
				else:
					print('ERROR: inserted data type is invalid. Please insert an integer.\n')
		elif i == '[':
			if data[data_index] == 0:
				count=0
				chk=0
				while True:
					count += 1
					if command_index+count >= len(commands):
						print('ERROR: one or more \']\' are missing in your input string. Program terminated.')
						commands = []
						break
					if commands[command_index+count] == ']' and chk == 0:
						break
					if commands[command_index+count] == ']' and chk != 0:
						chk -= 1
					if commands[command_index+count] == '[':
						chk += 1
				command_index += count
		elif i == ']':
			if data[data_index] != 0:
				count=0
				chk=0
				while True:
					count += 1
					if command_index-count <= 0:
						print('ERROR: one or more \'[\' are missing in your input string. Program terminated.')
						commands = []
						break
					if commands[command_index-count] == '[' and chk == 0:
						break
					if commands[command_index-count] == '[' and chk != 0:
						chk -= 1
					if commands[command_index-count] == ']':
						chk += 1
				command_index -= count
		command_index += 1
		if iteration != -1 and stopper > iteration:
			break
	if len(output) > 0:
		print('Program correctly executed. The output string is:\n')
		print(output)
		print()
	
	
print("Welcome to the Brainfuck language interpreter! ------ v0.3.1 alpha release")
print("Type 'help' for list of avaiable commands")
commands = []
output_char=False
while True:
	inp = input('>>>')
	if inp == 'exit':
		break
	elif inp == 'help':
		print("\n'filelaunch <name>' = execute instructions contained in the file <name>")
		print("\n'launch <instructions>' = execute instructions from keybord input")
		print("\n'outmode <type>' = choose output mode ('int' = integers, 'char' = characters) (default mode is set to 'int')")
		print("\n'exit' = close the program\n")
	elif inp[:11] == 'filelaunch ':
			file_input(inp[11:])
			execute(output_char)
	elif inp[:7] == 'launch ':
		commands = inp[7:]
		execute(output_char)
	elif inp == 'outmode char':
		output_char=True
	elif inp == 'outmode int':
		output_char=False
	else:
		print("ERROR: invalid command\n")
	inp=0