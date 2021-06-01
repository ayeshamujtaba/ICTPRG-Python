
file1 = open('names.txt', 'r')
file2 = open ('names-formatted.txt' , 'a')
lines = file1.readlines()
length = len(lines)
for i in range (length):
   file2.write(lines[i].capitalize())

file1.close
file2.close