
def solution(number):

	return sum([i if i % 3 == 0 or i % 5 == 0 else 0 for i in range(0 , number)])

# Link: https://www.codewars.com/kata/514b92a657cdc65150000006
