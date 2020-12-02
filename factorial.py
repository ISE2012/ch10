def fact(n): 
    #define the base case
    if(n==1):
        return 1
    else:
        # recursive case
        # n! = n * (n-1)
        return n * fact(n-1)

result = fact(9) #3!=3*2*1
# 9!=9*8*7*6*5*4*3*2*1
print(result)