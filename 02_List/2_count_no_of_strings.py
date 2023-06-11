# Write a Python to count the number of strings where the
# string length is 2 or more and the first and last character are same
# from a given list of the strings.

list1 = ["did", "gone", "hello", "john"]
count = 0
for i in list1:
    if i[0] == i[-1]:
        count += 1
print(count)
