sum = 0.0
number = input("Enter a number or press x to finish ")
while (number != 'x'):
    sum = sum+int(number)
    number = str (input("Enter a number or press x to finish "))
print ("The sum is" + str (sum))