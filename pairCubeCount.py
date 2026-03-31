import math

# def countPairs(n):
#     sum = 0
#     a = 0
#     b=0
#     for a in range(1,n+1):
#         for b in range(1,n+1):
            
#             if (a**3 + b**3 == n and a != b):
            
#                 sum +=1
#     return sum
# n = 91
# print(countPairs(n))
    



# much more efficient way o(n^1/3)
def count_pairs(n):
    
    
    
    count = 0
    
    
    for i in range(1,int(math.pow(n,1/3))+1):
        diff = n - i**3
        
        cbrt_diff = round(diff ** (1/3))
        
        if cbrt_diff**3 == diff:
            count += 1
    return count
            
        
if __name__ == "__main__":
  n = 2
  print(count_pairs(n))


