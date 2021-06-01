numberlist = []
digits = []
large = str (input ("Enter a large number: "))
for x in (large):
    x = int (x)
    digits.append(x) 
sum = 0
for k in range (0 , len(digits)):
    sum = digits[k] + sum 

print ("The sum of the digits: " , end = " ")

for l in range (len(digits)):
    print (digits[l] , end= " ")

print ("= " , sum)
