import timeit

start = timeit.default_timer()

nNumbers = 100
diff     = 0
sum      = 0

for i in range (1,nNumbers+1):
    sum = sum + i

for j in range (1,nNumbers+1):
    diff = diff + j*(sum-j)

stop = timeit.default_timer()
print('Runtime:', stop-start)
print('Answer is:', diff)