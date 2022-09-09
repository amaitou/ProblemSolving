
def is_isogram(string):


	lowercase = "".join(i.lower() for i in string)
	result = 0

	for i in lowercase :

		if lowercase.count(i) != 1 :

			result += 1

		else :

			pass

	if result != 0 : return False
	else : return True

# Link: https://www.codewars.com/kata/54ba84be607a92aa900000f1
