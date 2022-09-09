
#d = {"a" : 1 , "e" : 2 , "i" : 3 , "o" : 4 , "u" : 5}
a = ["a" , "e" , "i" , "o" , "u"]
b = ["1" , "2" , "3" , "4" , "5"]

def encode(st):
	
	global result
	result = ""
	
	for i in st :

		if i in a : result += str(a.index(i) + 1)
		else : result += i

	return result

def decode(st) :

	result2 = ""
	for i in st :
		
		if i == "1" : result2 += "a"
		elif i == "2" : result2 += "e"
		elif i == "3" : result2 += "i"
		elif i == "4" : result2 += "o"
		elif i == "5" : result2 += "u"
		else : result2 += i

	return result2

# Link: https://www.codewars.com/kata/53697be005f803751e0015aa/
