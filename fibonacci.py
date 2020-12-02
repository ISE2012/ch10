def fibonacci_recursive(n):
    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    
def main():
    x = 10 # compute the x-th Fibonacci number
    for i in range(x):
        result = fibonacci_recursive(i)
        print(result,end=", ")
    
# run main()
main()

