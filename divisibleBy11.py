


def divsibleBy11(n):
    even_sum = 0
    odd_sum = 0
    
    for i in range(len(n)):
        digit = int(n[i])
        if i % 2 == 0:
            odd_sum += digit
        else:      
            even_sum += digit
            
    
    
    
    diff = even_sum - odd_sum
    
    return ((odd_sum - even_sum) % 11 == 0 )
    
    return False
def divBy11(n):
    
    n = int(n)
    return  n % 11 ==0
  
if __name__ == "__main__":
    s = "76945"

    if divBy11(s):
        print("true")
    else:
        print("false")  

    s = "76945"
    print("true" if divsibleBy11(s) else "false")


