def prime(n):
 for num in range(0,n):
    for i in range(2,num):
        if (num%i==0):
            break
        else:
            print(num)
            break
prime(101)            