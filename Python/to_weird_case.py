
def to_weird_case(string):

	a = string.split(" ")
	b = ""
	r = []

	for i in a :
		for j in range(len(i)) :
			if j % 2 == 0 :
				b += i[j].upper()
			else :
				b +=i[j].lower()
		r.append(b)
		b = ""
	return " ".join(i for i in r)

# Link: https://www.codewars.com/kata/52b757663a95b11b3d00062d
