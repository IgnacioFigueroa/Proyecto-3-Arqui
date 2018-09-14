def PrintError(string):
    print string + ",ERROR"


file = open("opcode.txt", "r")
codes = list()
# Pasa el archivo a una lista de listas formato
for line in file:
    codes.append(tuple(list(line.strip().split('-'))))
fileName= raw_input("Ingrese el nombre del archivo: ")
file = open(fileName)
program = list()
labels = list()
# Hace una lista con todas las lineas del archivo
for line in file:
    program.append(line.strip().replace("\t", ""))
file.close()
# Mete los labels a una lista y los asocia con el numero de linea en el que estan
for line in program:
    ind=program.index(line)
    lineWithLabel = line.split(':')
    if len(lineWithLabel) > 1:
        labels.append((lineWithLabel[0], ind))
    program[ind] = lineWithLabel[-1]
#Reemplazo lo que esta dentro del parentesis por un DIR

for line in program:
    print line
    ind = program.index(line)
    if "(" in line and ")" in line and "(A)" not in line and "(B)" not in line:
        start=line.index('(')+1
        while line[start] != ')':
            line = line.replace(line[start], "")
            program[ind] = line
        print "linea", line
        program[ind]= line[:line.index('(')+1]+"DIR"+line[line.index(')'):]
        print "linea2: ", program[ind]
    if line.find(',') != -1:
        if line[line.index(",")+1:].isdigit():
            line = line[: line.index(",")+1] + "LIT"
            program[ind] = line
    if line[0] == 'J' and line.find(',')==-1:
        line = line.split(" ")
        flag=True
        for label, indexLabel in labels:
            if line[1]==label:
                flag=False
        if flag:
            PrintError("LABEL NOT ENCOUNTERED")
        else:
            line[1] = "DIR"
        s = " "
        s = s.join(line)
        program[ind]=s
print codes
print program
flag = True
archivo = open(fileName.replace(".txt", ".out"), "w")
cont=0
for line in program:
    flag=True
    for ins, opcode in codes:
        if ins == line:
            flag = False
            archivo.write(opcode+ "\n")
            cont+=1
    if flag:
        PrintError("INSTRUCTION "+line+" DOES NOT EXISTS")
if cont!=len(program):
    PrintError("ARCHIVO ASEMBLY NO VALIDO")
archivo.close()

