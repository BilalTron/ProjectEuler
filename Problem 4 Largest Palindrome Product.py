import timeit

# Checks if six-digit number is Palindromic
def isPalindrome(n):
    return ( int(n/1e5)%10 == n%10 and \
             int(n/1e4)%10 == int(n/1e1)%10 and \
             int(n/1e3)%10 == int(n/1e2)%10 )

start = timeit.default_timer()

maxPal = 100001

for i in range(999,100,-1):
    for j in range(i,100,-1):
        ij = i*j
        if ij > maxPal:
            if isPalindrome(ij):
                maxPal = ij


stop = timeit.default_timer()

print('Runtime:', stop-start)
print('Answer is', maxPal)