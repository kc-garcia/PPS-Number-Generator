from random import randint;

def generatorPPS(letter = 'A'):
	# https://en.wikipedia.org/wiki/Personal_Public_Service_Number
	# Generates PPS Number in the format of seven numeric characters (including leading zeros)
	# a check character and a second letter, given by the user, default is A (for individuals)

	ppsWeight = [8, 7, 6, 5, 4, 3, 2 ,9]
	pps = []
	letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 0}
	
	# Generates 7 random number in range 0 to 9 and store in a list
	for i in range (7):
		pps.append(randint(0, 9))
	# Store second letter given by the user in list postion 9
	pps.insert(8, letter)
	#Each digit is multiplied by a weight defined in ppsWeight
	#with a weighting of 9 assigned to the numeric equivalent of the alphabetic character in position 9 and sum stored in checkChar
	checkChar = 0
	for index, value in enumerate(pps):
		if isinstance(value,str):
			checkChar += letters[value]*ppsWeight[index]
		else:
			checkChar += value*ppsWeight[index]
	#The modulus 23 of checkChar indicate the check character position in the alphabet
	#Loop through dictionary of letters to find the key(letter) equivalent for the remainder
	for key, value in letters.items():
		if value == checkChar%23:
			pps.insert(7,key)
	#Transfor int to string and return a PPS Number in a string formart
	ppsNumber = [str(i) for i in pps]
	return ''.join(ppsNumber)

def checkPPS(pps):
	#Check PPS Number and return a bool value, True = Valid PPS Number False = Invalid PPS Number

	#It is a invalid PPS number if pps is not between 8 and 9 character long,
	#the first 7 characters are not number
	#at least the last character is a letter
	if not 8>= len(pps) <=9 or not pps[:8].isdigit() or not pps[-1].isalpha():
		return False

	ppsWeight = [8, 7, 6, 5, 4, 3, 2 ,9]
	letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 0}

	#Transfor string into list of int and str
	ppsNumber = [int(character) if index < 7 else character for index, character in enumerate(pps)]
	#Each digit is multiplied by a weight defined in ppsWeight
	#with a weighting of 9 assigned to the numeric equivalent of the alphabetic character in position 9 and sum stored in checkChar
	checkChar = 0
	for index, value in enumerate(ppsNumber):
		if isinstance(value,str):
			if index == 7:
				continue
			else:
				checkChar += letters[value]*ppsWeight[-1]
		else:
			checkChar += value*ppsWeight[index]
	#The modulus 23 of checkChar indicate the check character position in the alphabet
	#Loop through dictionary of letters to find the key(letter) equivalent for the remainder
	#compare key with the check letter in position 8 of PPS Number, if match is a valid PPS Number
	for key, value in letters.items():
		if value == checkChar%23:
			if key == ppsNumber[7]:
				return True
	return False

listPPS = []
for i in range (0,50):
	listPPS.append(generatorPPS())
