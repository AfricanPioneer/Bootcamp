def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
     temp = a
     a = b
     b = temp + b
    return a

num = input("Please enter a number to get its fibonacci series ")
for c in range(0, num):
    print(fibonacci(c))
