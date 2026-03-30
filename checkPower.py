

def isPower(x,y):
    ran = 0
    
    if x == 1 and y!= 1:
        return False
        
    if y ==1:
       return True
    else:
    
    
        while y!= 1:
            if y % x != 0:
                return False
            y = y // x  
            ran += 1
        
        
        return True





if __name__ == '__main__':
    print(isPower(10, 1))
    print(isPower(1, 20))
    print(isPower(2, 128))
    print(isPower(2, 30))