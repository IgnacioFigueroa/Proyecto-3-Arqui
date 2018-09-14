file = open("opcode.txt", "r")
instructions = list()
for line in file:
    instructions.append(list(line.strip().split('-')))
for tupla in instructions:
    tupla[1] = tuple(tupla[1].split(','))
print instructions

file.close()
file = open("assembly.txt")
program=list()

