def f(n):
    print(n)
    if n == 0: #base case
        return 0
    else:
        #recursive case
        return 1 + f(n-1) 

#f(0)
#f(1)
#f(2)
f(100)
#print(result)