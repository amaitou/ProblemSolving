
def persistence(num) :

	s = str(num)
	result = 1
	counter = 0

	if len(s) == 1 : 

		return 0
	
	else :
		
		while len(s) != 1 :

			_m = [int(i) for i in s]
			for i in _m :
				result *= i

			s = str(result)
			result = 1
			counter += 1

		return counter

# Link: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
