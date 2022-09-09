
def move_zeros(array):

	#return sorted(array, key=lambda x: x==0 and type(x) is not bool)
	a = []
	b = []

	for i in array :
		if not (type(i) in [int , float] and i == 0) :
			a.append(i)
		else :
			b.append(0)

	return a + b

# Link: https://www.codewars.com/kata/52597aa56021e91c93000cb0
