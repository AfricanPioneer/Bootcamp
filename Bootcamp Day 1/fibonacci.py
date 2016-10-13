#Function to list fibonacci series
def fibonacci(n):

    if n == 0:
     return 0
    elif type(n) is not int:
        raise TypeError
    elif n<0:
        raise ValueError

     # Initialize first two fibonacci numbers
    fib1 = 0
    fib2 = 1
    lst = []

    # Add the last number and second last number
    for i in range(n):
        lst.append(fib1)
        nextNum = fib1 + fib2
        fib2 = fib1
        fib1 = nextNum
    return(lst)

#num = input("Please enter a number to get its fibonacci series ")
#for c in range(0, num):
 #   print(fibonacci(c))
