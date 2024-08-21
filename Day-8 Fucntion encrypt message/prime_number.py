def prime_checker(num):
    prime_checker = True
    for i in range(2,num):
        if num % i == 0:
            prime_checker = False
            
    if(prime_checker == True):
        print("Prime Number")
    else:
        print("Not a prime number")     
prime_checker(5)