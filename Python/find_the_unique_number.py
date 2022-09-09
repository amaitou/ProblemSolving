def find_uniq(arr):
    # your code here
    arr.sort()

    if(arr[0] < arr[len(arr)-1] and arr[0] < arr[len(arr)-2]):
        n = arr[0]
    else:
        n = arr[len(arr)-1]


    return n

# Link: https://www.codewars.com/kata/55f81f9aa51f9b72a200002f

