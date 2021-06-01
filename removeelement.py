#list has duplicates
x4 = [2.5, 'a', 7, 'abc', 46, 7]
x4.remove(7)
print (x4)
x4.remove(7)
print (x4)
#x4.remove("def")
#print (x4)
#another way of deleting - will delete last element in the list
x4.pop(-1)
print (x4)