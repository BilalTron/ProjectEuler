import timeit

#Solution 1: Sieve of Eratothenes

start = timeit.default_timer()

# implement Sieve of Eratosthenes
def sieve(n):

    listofprimes    = [1] * (n+1)
    listofprimes[0] = 0
    # all even numbers are not prime, except 2
    for k in range(4,n,2):
        listofprimes[k] = 0

    # going through the odd numbers only:
    # all multiples of prime numbers are not prime (with optimizations)
    for i in range(3,n,2):
        if listofprimes[i] == 1:
            j = i*i
            while j <= n :
                listofprimes[j] = 0
                j = j + i
    return listofprimes

primes = sieve(1000000)

stop = timeit.default_timer()

order = 0
ip    = 0
for p in primes:
    if primes[p] == 1:
        if order == 10001:
            print(order,'th prime number is', ip)
        order = order + 1
    ip = ip + 1

print('Runtime of Sieve:', stop-start)

#Solution 2: Naive

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

start = timeit.default_timer()

order = 0
num   = 2
while order < 10001:
    if isprime(num):
        order = order +1
    num = num + 1

stop = timeit.default_timer()

print('Runtime of Naive:', stop-start)
print('Answer is:', num-1)
