import timeit


start = timeit.default_timer()

sum  = 2
num1 = 1
num2 = 2
fib  = num1 + num2
while fib < 4e6 :
    if fib%2 == 0:
        sum = sum + fib
    num1 = num2
    num2 = fib
    fib = num1 + num2 

stop = timeit.default_timer()

print('Runtime:', stop-start)
print('Sum is', sum)