import fileinput
res = 0
for line in fileinput.input():
	line = line.replace('\n', '')
	res += float(line)
if res.is_integer() == True:
	print(int(res))
else:
	print(res)
