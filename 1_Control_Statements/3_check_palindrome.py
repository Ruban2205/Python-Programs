# Write a python program to check whether the number is palindrome or not

num = int(input("Enter any number: "))

reverse = 0
temp = num

while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10

if num == reverse:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
