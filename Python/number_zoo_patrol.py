def find_missing_number_2(numbers) :

	r = int("".join(str(i) if not i in numbers else "" for i in range(1 , max(numbers) + 2)))
	return int(str(r)[0])

# Link: https://www.codewars.com/kata/5276c18121e20900c0000235
