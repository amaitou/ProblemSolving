
def sum_arrays(array1,array2):

	if array1 == array2 == [] :
		return []
	elif array1 == [] :
		return array2
	elif array2 == [] :
		return array1
	else :
		a = int("".join(str(i) for i in array1))
		b = int("".join(str(i) for i in array2))

		c , r , x = "" , [] , str(a + b)

		for i in x :
			if i == "-" :
				c = '-'
			elif len(r) == 0 and c == "-" :
				r.append(-int(i))
				c = ""
			else :
				r.append(int(i))

	r = r.remove(0) if r[0] == 0 and len(r) > 1 else r
	return r

# Link: https://www.codewars.com/kata/59c3e8c9f5d5e40cab000ca6
