


def reverseDigit(n):
    
    reversed_digit = 0
    while n!= 0:
        last_dig = n % 10
        n= n // 10
        
        reversed_digit = reversed_digit * 10 + last_dig
    return reversed_digit
  
  
  
  
print(reverseDigit(456200))