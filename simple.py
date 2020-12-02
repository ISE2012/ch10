def compute(intInput):
    print(intInput)
    if(intInput>2): #until this is false
        # recursive case
        newinInput = intInput-1
        print("compute("+str(newinInput)+")")
        # calls itself
        compute(newinInput)

def main():
    compute(50)

main()