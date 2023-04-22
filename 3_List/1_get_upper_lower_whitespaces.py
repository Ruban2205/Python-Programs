# Write a python funcrions to print Uppercase, Lowercase and Whitespaces.

string = input("Enter any string: ")


def function(string):
    upper = 0
    lower = 0
    whitespace = 0
    for i in string:
        if 65 <= ord(i) <= 90:
            upper = upper + 1
        elif 97 <= ord(i) <= 122:
            lower = lower + 1
        elif ord(i) == 32:
            whitespace = whitespace + 1

    print("The number of uppercase are", upper, "lowercase are", lower, "whitespaces are", whitespace)


function(string)
