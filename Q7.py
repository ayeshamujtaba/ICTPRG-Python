number = 0
num = []
rpt = []
while (number != 'x'):
    number = input ("Enter a number or press x to finish: ")
    num.append(number)
num.pop(-1)

for i in range(0, len(num)):  
    for j in range (i+1, len(num)):  
        if(num[i] == num[j]):  
            rpt.append (num[j])

for k in range (0 , len(rpt)):
    rpt[k] = int (rpt[k])
print(str(rpt))