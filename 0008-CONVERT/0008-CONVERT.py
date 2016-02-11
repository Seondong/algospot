def unit1tounit2(argument):
    switcher = {
        "kg": "lb",
        "lb": "kg",
        "l": "g",
        "g": "l"
    }
    return switcher.get(argument)

for i in range(input()):
	line = raw_input()
	val = float(line.split()[0])
	unit= line.split()[1]

	newunit = unit1tounit2(unit)
	
	if newunit == "lb":
		newval = val * 2.2046
	elif newunit == "kg":
		newval = val * 0.4536
	elif newunit == "g":
		newval = val * 0.2642
	elif newunit == "l":
		newval = val * 3.7854

	print i+1, format(round(newval, 4), '.4f'), newunit