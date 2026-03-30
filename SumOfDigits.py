


def sumOfDigits(n):
    sum = 0
    while n!= 0:
        last = n%10
        sum+= last
        n //=10
    return sum
    
        
if __name__ == "__main__":
	n = 1234
	print(sumOfDigits(n)) 
    



