def narcissistic( value ):
    
    return True if sum([int(i) ** len(str(value)) for i in str(value)]) == value else False

# Link: https://www.codewars.com/kata/5287e858c6b5a9678200083c

