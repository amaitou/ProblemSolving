def rgb(r, g, b):
    

    l = [r , g , b]
    for i in range(len(l)) :
    	if l[i] > 255 :
    		l[i] = 255
    	else :
    		pass
    
    r = ""

    for i in l :

    	if i >= 0 and i <= 9 :
    		r += "0" + str(i)
    	elif i < 0 :
    		r += "00"
    	else :
    		r += hex(i).replace("0x" , "").upper()

    return r

# Link: https://www.codewars.com/kata/513e08acc600c94f01000001
