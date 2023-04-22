# Write a python functions to find whether a given number is perfect or not.

def perfect_number(n):
    x = 0
    for i in range(1, n):
        if n % i == 0:
            x += i
    if x == n:
        print("It is a perfect number")
    else:
        print("It is not a perfect number")
    return x == n


n = int(input("Enter a number: "))

perfect_number(n)
