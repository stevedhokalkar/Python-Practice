#Q3) Python | Sort a List according to the Length of the Elements

# define a function
def Sorting(list):
	sorted_list = sorted(list, key=len)# to find the sorted list from the list
	return sorted_list #return a sorted values
	
#Given a input values
list = ["rohan", "amy", "sapna", "muhammad", "aakash", "raunak", "chinmoy"]

#print the value
print(Sorting(list))

