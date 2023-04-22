# Write a python function to use arbitarary function by getting a
# sequence of numbers as input and only print the divisors of last input
# from the passed numbers

def last(*listn):
    i = 1
    while (i <= listn[-1]):
        if (listn[-1] % i == 0):
            print(i, end=' ')
        i = i + 1


last(1, 2, 3)
last(4, 5, 6, 7)
last(8, 9, 10, 11, 12)