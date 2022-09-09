def letter_count(s):
    d = {}
    for i in s:
        if i in d.keys():
            d[i] = d[i] + 1
        else:
            d[i] = 1
    return d

# Link: https://www.codewars.com/kata/5808ff71c7cfa1c6aa00006d

