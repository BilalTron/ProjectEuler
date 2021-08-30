import timeit

# Solution 1 

start = timeit.default_timer()

multiple = 1
stop     = 1000
sum      = 0

multFive = multiple*5

while (multFive) < stop:
    multThree = multiple*3
    sum       = multFive + sum
    if multThree % 5 != 0:
        sum = sum + multThree
    multiple = multiple + 1
    multFive = multiple*5
     
multThree = multiple*3

while (multThree) < stop:
    if multiple%5 != 0:
        sum = multThree + sum
    multiple = multiple + 1
    multThree = multiple*3

stop = timeit.default_timer()

print('Runtime:', stop-start)
print('Sum is', sum)

# Solution 2

start = timeit.default_timer()

sum2 = 0

for i in range(1000) :
    if bool(i%3==0) or bool(i%5==0): #exclusive or
        sum2 = sum2 + i

stop = timeit.default_timer()

print('Runtime:', stop-start)
print('Sum is', sum2)