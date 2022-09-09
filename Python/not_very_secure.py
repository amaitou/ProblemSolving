
def alphanumeric(password):

	result = 0

	if password == "" : return False
	
	else :
		
		for i in password :

			var = ord(i)

			if var > 47 and var < 58 : result += 1
			elif var > 64 and var < 91 : result += 1
			elif var > 96 and var < 123 : result += 1
			else : result += 0

	if len(password) == result : return True
	else : return False

# Link: https://www.codewars.com/kata/526dbd6c8c0eb53254000110
