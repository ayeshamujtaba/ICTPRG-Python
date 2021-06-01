count = 1
while (count >=1):
    number = int (input ("Enter a number"))
    if (number >=50 and number <=70):
        print ("Number within Range.")
        count = 0
    else:
        print ("Number not within range.")
        count = count+1
