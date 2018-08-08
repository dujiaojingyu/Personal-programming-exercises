digital = []
def get_digits(n):

    if n > 0:
        digital.insert(0,n%10)
        get_digits(n//10)

       
get_digits(12345)
print(digital)
