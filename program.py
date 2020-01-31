import fileinput
lines = []
for line in fileinput.input():
	line = line.replace('\n', '')
	line = float(line)
	lines.append(line)
res = sum(lines)
if res.is_integer() == True:
	print(int(res))
else:
	print(res)
