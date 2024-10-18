#Q1) write a Python program to swap the first and last element of the list using Python.

# list of input values
list=["Python","Data Analytics","SQL","Java"]

# swap the first element with last element by swapping the list element by index number
list[0], list[-1] = list[-1], list[0]

#print the value by print statements
print("The Value after swapping will be: ",list)


