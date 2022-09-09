
def likes(names) :


	if len(names) == 0 :

		return "no one likes this"

	elif len(names) == 1 :

		return "".join(names) + " likes this"

	elif len(names) > 1 and len(names) < 4 :

		result = ""

		for i in names :

			if i == names[-1] :

				result += "and "
				result += i
				result += " "

			elif i == names[-2] :

				result += i
				result += " "

			else :

				result += i
				result += ", "

		return result + "like this"

	else :

		result = ""

		for i in names :

			if i == names[0] :

				result += i
				result += ", "

			elif i == names[1] :

				result += i
				result += " and "

			else :

				pass

		return result + str(len(names) - 2) + " others like this"
	
# Link: https://www.codewars.com/kata/5266876b8f4bf2da9b000362
