name = str (input ("Enter your name: "))
insertlist = []
hold = name.split(" ")
length = int (len (hold))
for i in range (length):
    insertlist.insert(i, hold[i][0])
print ("Initials: " , end = "")
for k in (insertlist):
    print (k.upper(), end= "")