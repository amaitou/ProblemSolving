def comp(array1 , array2) :
    return False if array2 == None or array1 == None else sorted([i ** 2 for i in array1]) == sorted(array2)

# Link: https://www.codewars.com/kata/550498447451fbbd7600041c

