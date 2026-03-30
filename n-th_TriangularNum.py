

def n_th_Term(n):
    num = 1
    sum = 0
    while (num <= n):
        sum += num
        num+=1
    return sum


if __name__ == "__main__":                                                                                                                                               
    print(n_th_Term(4))
    print(n_th_Term( 10 ))
     