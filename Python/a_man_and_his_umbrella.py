def min_umbrellas(weather):
    work = home = 0
    for i , e in enumerate(weather, 0):
        if i % 2 == 0 and (e in ["rainy", 'thunderstorms']):
            work += 1
            home -= home > 0
        elif i % 2 != 0 and (e in ["rainy", 'thunderstorms']):
            home += 1
            work -= work > 0
    return work + home

# Link: https://www.codewars.com/kata/58298e19c983caf4ba000c8d

