factorial = 1
file = open ('factorial.txt' , 'a')
for num in range (10):
    if num == 0:
        file.write ("\n")
    elif num > 0:
        for i in range(1,num + 1):
            factorial = factorial*i
    print(num,"--->",factorial)
    file.write("%d ----> %d \n"  % (num,factorial))

file.close