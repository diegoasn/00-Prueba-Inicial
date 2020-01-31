import fileinput
lines = []
for line in fileinput.input():
    line = line.replace('\n', '')
    line = float(line)
resultado = sum(lines)
if resultado.is_integer() == True:
	print(int(resultado))
else:
	print(resultado)
