



def toBinary(n):
    b = []
    while n>0:
        remainder = n%2
        b.append(remainder)
        n //= 2
    b.reverse()
    return b
    

        
        


if __name__ == "__main__":
    n = 12
    print(toBinary(n))


