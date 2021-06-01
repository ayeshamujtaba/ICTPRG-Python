sum = 0
number = 0
num_int = 0
final_sum = 0

while (number != 'x'):
    
    print ("The sum is", final_sum)
    number = input("Enter number")
    if (number == 'x'):
        print ("The sum is", final_sum)
    else:
        num_int = int (number)
        final_sum = final_sum + number
print ("The sum is", final_sum)