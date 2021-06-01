factorial = 1

for num in range (10):
    if num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
    print(num,"--->",factorial)
