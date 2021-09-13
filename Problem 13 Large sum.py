import timeit

start = timeit.default_timer()

number = []

for i in range(50):
    f = open("Problem13input.txt", "r")
    print(f.readline())
    number.append( int(f) % 1e10 )


stop = timeit.default_timer()
print('Runtime:', stop-start)
print('Answer is:', )