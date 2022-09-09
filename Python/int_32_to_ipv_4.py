def int32_to_ip(int32) :

    return f"{int(int32 / 16777216) % 256}.{int(int32 / 65536) % 256}.{int(int32 / 256) % 256}.{int(int32) % 256}"

# Link: https://www.codewars.com/kata/52e88b39ffb6ac53a400022e
