
def expanded_form(num):

	c = 1
	l = "".join(i for i in str(num))
	s = ""
	a = []
	
	for i in l :

		r = l[c:]
		s += i

		for j in r :

			s += "0"

		a.append(s)
		s = ""
		c += 1

	
	for i in a :

		if i ==  "0" * len(i) :

			pass

		else :

			s += i
			s += " + "

	return s[:-2]

# Link: https://www.codewars.com/kata/5842df8ccbd22792a4000245
