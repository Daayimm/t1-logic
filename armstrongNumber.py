
def armstrongNum(n):
    arr = []
    sum = 0
    original = n
    while n != 0:
        last = n % 10
        n //= 10
        arr.append(last)

    length_of_array = len(arr)
    
    for i in arr:
        i **= length_of_array
        sum += i
        
    
    return sum == original


def armstrong(n):
    number = str(n)
    power = len(number) 
    sum = 0
    for c in number:
        sum += (int(c) ** power)
    return sum == n
    
    
    
if __name__ == "__main__":
    n = 153
    if armstrongNum(n):
        print("true")
    else:
        print("false")  
    
    if armstrong(n):
        print("true")
    else:
        print("false")  
        
    
    




