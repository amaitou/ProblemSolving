
def divisors(integer):

	r = [i if integer % i == 0 else "p" for i in range(2 , integer)]
	s = []
	if len(r) == r.count("p") : return str(integer) + " is prime"
	else : 
		for i in r :
			if i != "p" : s.append(i)
	return s

# Link :https://www.codewars.com/kata/544aed4c4a30184e960010f4

