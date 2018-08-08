def gcd_test_two(a, b):  
    if a>b:  
        a, b=b, a  
    if b%a==0:  
        return a  
    else:  
        return gcd_test_two(a,b%a)  
