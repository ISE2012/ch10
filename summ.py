def summ(num):
    if(num==0):
        return 0
    else:
        return num + summ(num-1)
    
def main():
    result = summ(4) 
    # sum(4)+sum(3)+sum(2)+sum(1)+sum(0)
    print(result)
    
main()