v = [2,-5,12,13]
length = len(v)
max = v[0]
i = 0
while (i < length):
    if (max < v[i]):
        max = v[i]
    i = i+1
print ("The maximum number is " ,max)

