
def gcd(a,b):
    if b == 0:
        return a
    else:
        while a%b != 0:
            a , b = b , a%b

            if a%b == 0:
                
                return b
       
    
