
def unique_in_order(iterable):
	
	r = []
	for i in iterable :
		if len(r) == 0 or i != r[-1] :
			r.append(i)
	return r

# Link: https://www.codewars.com/kata/54e6533c92449cc251001667
