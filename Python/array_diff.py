
def array_diff(a, b):
	
	r = []
	#s = "".join(str(i) for i in b)
	
	for i in a :

		#si = str(i)

		if not i in b : r.append(i)

	return r


# Link: https://www.codewars.com/kata/523f5d21c841566fde000009

