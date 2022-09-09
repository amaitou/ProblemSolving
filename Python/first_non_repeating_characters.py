
def first_non_repeating_letter(string) :

	s = string.lower()

	for i in s :
		if s.count(i) == 1 :
			return string[s.index(i)]

	return ""

# Link: https://www.codewars.com/kata/52bc74d4ac05d0945d00054e
