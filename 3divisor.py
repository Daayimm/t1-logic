

def is_prime(n):
    
    for i in range (2,n-1):
        if n % i == 0:
            return False
    return True

def exactlyThreeDivisors(n):
    
    count = 0
    num = []
    
    for i in range(2,int(n**(1/2)+1)):
        primecheck = is_prime(i)
        if int(primecheck):
            num.append(i)
            count += 1
            
    
    return count,num


if __name__ == "__main__":
    n = 100
    ans = exactlyThreeDivisors(n)
    print(ans)
            
        