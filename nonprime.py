def notPrime(val):
    isPrime = False
    if val==1:
        return True
    elif(val==2 or val==3):
        return False
    else:
        sqr_val = int((val ** 0.5) // 1)        
        for i in range(2,sqr_val+1):
            if (val%i==0):
                isPrime = True
                break
    return isPrime

def noPrim(n):
    for i in range(1,n+1):
        if (notPrime(i)):
            yield i

def notPrime(val):
    isPrime = False
    if val==1:
        return True
    elif(val==2 or val==3):
        return False
    else:
        sqr_val = int((val ** 0.5) // 1)        
        for i in range(2,sqr_val+1):
            if (val%i==0):
                isPrime = True
                break
    return isPrime
def manipulate_generator(generator, n):
  	# Enter your code here
    while (not notPrime(n+1)):
        n=next(generator)

print(next(noPrim(6)))

