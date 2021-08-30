# Solution is simple:
# answer is a multiplication of some of the numbers from 1 to 20
# going through the numbers: 1, everything divisible by it
#                            2, multiply by 2, prime
#                            3, multiply by 3, prime
#                            4, multiply by 2, there's already another 2 which gives 4
#                            5, multiply by 5, prime
#                            6, already have 2*3
#                            7, multiply by 7, prime
#                            8, multiply by 2, already *4
#                            9, multiply by 3, already *3
#                            10, already have 2*5
#                            11, multiply by 11, prime
#                            12, already have 2*3*2
#                            13, multiply by 13, prime
#                            14, already 7*2
#                            15, already 3*5
#                            16, multiply by 2, already 2*2*2
#                            17, multiply by 17, prime
#                            18, already 3*3*2
#                            19, multiply by 19, prime
#                            20, already 2*5*2

print('Answer is', 2*3*2*5*7*2*3*11*13*2*17*19)