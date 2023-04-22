# Write a python program to check whether the number is prime or not

num = int(input("Enter any number: "))
if num > 1:
    for i in range(2, num):
        if(num % i) == 0:
            print("The given number ", num, " is not a prime number")
            break
    else:
        print("The given number ", num, " is a prime number")
else:
    print("The given number ", num, "is not a prime number")
