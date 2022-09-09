
def reverse_alternate(string):

	result = ""
	counter = 0
	liststr = string.split(" ")

	for i in range(liststr.count("")) :

		liststr.remove("")

	for i in liststr :

		if not i.isalpha() :

			pass

		if liststr.index(i) % 2 != 0 :

			result += i[::-1]
			result += " "

		else :

			result += i
			result += " "

	return result.strip()

# Link: https://www.codewars.com/kata/58d76854024c72c3e20000de
