frst_number = int (input ("Enter First number"))
sc_number = int (input ("Enter second number"))
result = frst_number + sc_number
f = open('maths.txt', 'w')
f.write (" The result is %d" % (result))
f.close

