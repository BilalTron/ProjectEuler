import timeit

# Note 1: every number above 1 is divisible by 1 and itself, no need to check.
# Note 2: only need to check numbers between 2 and sqrt(N). If N is divisible by a number in that range, it must be divisible by 2 numbers.

start = timeit.default_timer()

notfound = 1
triageN  = 28
order    = 8

while notfound:
    triageN  = triageN + order
    order    = order + 1
    divisors = 2
    for i in range(2, int(triageN**0.5)):
        if triageN % i ==0:
            divisors = divisors + 2

    if divisors > 500:
        notfound = 0

stop = timeit.default_timer()
print('Runtime:', stop-start)
print('Answer is:', triageN)