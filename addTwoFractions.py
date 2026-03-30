from math import gcd

def addTwoFractions(a,b):
    
    numerator = b[1] * (a[0] ) + a[1] * b[0]
    denominator = a[1] * b[1]
    
    g = gcd(numerator,denominator)

    numerator //= g
    denominator //= g
     
    return [numerator,denominator]
if __name__ == '__main__':
    a = [1, 2]
    b = [3, 2]
    print(addTwoFractions(a,b))




