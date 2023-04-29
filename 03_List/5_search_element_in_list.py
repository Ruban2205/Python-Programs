# Write a python function to search an element in the list. If
# the element is found the name of the element. If not, append the
# element to the list and return value.

def checkElements(a):
    list1 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for i in list1:
        if i == a:
            print("The Number is Exists in the List.")
            break
        else:
            print("The Number does not Exists.")
            list1.append(x)
            print("Updated list is: ", list1)
            break


x = int(input("\nEnter the number: "))
checkElements(x)
