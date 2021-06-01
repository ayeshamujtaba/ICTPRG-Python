number = 0
length = 0
numberlist = []
newnumberlist = []
while (number != 'x'):
    number = input ("Enter a number or press x to finish: ")
    numberlist.append(number)
numberlist.pop(-1)
length = len(numberlist)
for k in range (0 , length):
    numberlist [k] = int (numberlist[k])

print ("You Entered" , str (numberlist))