from random import randint;

def generatorPPS():
	ppsWeight = [8, 7, 6, 5, 4, 3, 2 ,9]
	pps = []
	letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22}
	for i in range (0,7):
		pps.append(randint(0, 9))
	pps.insert(8,'A')
	checkChar = 0
	for index, value in enumerate(pps):
		if isinstance(value,str):
			checkChar += letters[value]*ppsWeight[index]
		else:
			checkChar += value*ppsWeight[index]
	if checkChar%23 == 0:
		pps.insert(7,'W')
	else:
		for key, value in letters.items():
			if value == checkChar%23:
				pps.insert(7,key)
	return pps

listPPS = []
for i in range (0,50):
	pps = generatorPPS()
	for n in range (len(pps)):
		pps[n] = str(pps[n])
	listPPS.append(''.join(pps))
print(listPPS)