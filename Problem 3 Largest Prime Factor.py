import timeit

def isprime(numero):
    if numero == 1:
        return False

    sqrtnumero = int(numero**0.5)
    i = 2
    while i <= sqrtnumero:
        if numero % i == 0:
            return False
        i = i+1
    return True



maxfactor = 1
number    = 600851475143

start = timeit.default_timer()

# first for loop will find common factors
for i in range ( 2, int(number**0.5) ):
    # if divisible by i, check two numbers for a prime one
    if number%i == 0:
        fact2 = number/i
        if (isprime(fact2) and maxfactor < fact2):
            maxfactor = fact2
            break
        if (isprime(i) and maxfactor < i):
            maxfactor = i

stop = timeit.default_timer()

print('Runtime:', stop-start)
print('Answer is', maxfactor)