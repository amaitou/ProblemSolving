
def duplicate_count(text):

	result = 0
	string = ""
	lowercase = "".join(i.lower() for i in text)

	for i in lowercase :

		if lowercase.count(i) > 1 :
			if not i in string :
				string += i
				result += 1
			else :
				pass
		else :
			pass

	return result


# Link: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

