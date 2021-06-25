array = []
data = {}
with open("datosTrue.txt") as ins:
    for line in ins:
        array.append(int(line))
        if not(line.strip() in data):
        	data[line.strip()] = 0
        data[line.strip()] = data[line.strip()] + 1

chi_t = 2.4
total = 0
critical = 1073.64
for key in data.keys():
	term = (data[key] - 2.4)*(data[key] - 2.4)/2.4
	total = total + term

if total < critical:
	print("There is no reason to believe that this dataset does not follow a uniform distribution")
else:
	print("It is possible that this dataset does not follow a uniform distribution")


