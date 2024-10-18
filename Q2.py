#Q2) Interchange first and last elements using Temporary Value.

#Define the input value
newlist=[12,3,45,24]

# Swapping process
temp = newlist[0]
newlist[0] = newlist[-1]
newlist[-1]=temp

#printing the values
print(newlist)
