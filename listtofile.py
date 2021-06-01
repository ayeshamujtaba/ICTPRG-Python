# Writing to a files

# This is writing a list of lines as strings

#   to a file.

cities = [ "London\n", "Canberra\n", "Seol\n"]

file1 = open('myfile.txt', 'w')

file1.writelines(cities)

file1.close()



# Reading from a file

file2 = open('names.txt', 'r')

lines = file2.readlines()
length = len(lines)
print (length)
print(lines)

print()

#print the first element

for i in range (length):
   print (lines[i].capitalize())
#print(lines[2])