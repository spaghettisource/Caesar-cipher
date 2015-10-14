import string

def buildCoder(shift):

	lowercaseCharacters = string.ascii_lowercase
	uppercaseCharacters = string.ascii_uppercase
	allCharacters = lowercaseCharacters + uppercaseCharacters

	
	encrypted = {}


	def GetShift(character, charcase, shift):
		if charcase == True:
			charpostion = uppercaseCharacters.find(character) + 1
			if charpostion + shift > 26:
				return uppercaseCharacters[charpostion + shift - 27]
			else:
				return uppercaseCharacters[charpostion + shift - 1]
		else:
			charpostion = lowercaseCharacters.find(character) + 1
			if charpostion + shift > 26:
				return lowercaseCharacters[charpostion + shift - 27]
			else:
				return lowercaseCharacters[charpostion + shift - 1]
			
		


	for c in allCharacters:
		charcase = c.istitle() 
		encrypted[c] = GetShift(c, charcase, shift)
	
	return encrypted
		
		 
		
	
	

def applyCoder(text, coder):
	newtext = list(text)
	counter = 0
	
	for c in newtext:
		if c in coder:
			newtext[counter] = coder[newtext[counter]]
		counter += 1
	
	return ''.join(newtext)
		
print applyCoder("Hello, world!", buildCoder(3))
		
		