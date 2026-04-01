




def divBy13(n):
    
    
    
    turn = 0
    total = 0
    length_digit = len(n)
    while length_digit % 3 !=0:
        n += '0'
        length_digit = len(n)
            
    for j in range(0,length_digit,3):
        sliced = n[j:j+3]    
        turn += 1
        
        if turn % 2 == 0:
            sliced_int = 0-int(sliced)
           
            total += sliced_int
        else:
            sliced_int =int(sliced)
            total += sliced_int
    print(n)
        
    return (total % 13 == 0)
            
    
if __name__ == "__main__":
    s = "2911285"
    isDivisible = divBy13(s)
    
    if isDivisible:
        print("true")
    else:
        print("false")  