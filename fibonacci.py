# Write the function between the START and END tags
# START
def FibonacciAdder(num):
  # Check if input is 0 then it will
    # print incorrect input
    if num < 0:
        print("Incorrect input")
 
    elif num == 0:
        return 0
 
    elif num == 1 or num == 2:
        return 1
 
    else:
        a=0
        count=1
        catch =0
        sum=0
        hold =0
        b=1
        while(count <= num):
            hold = hold +sum
            print(sum, end = " ")
            count += 1
            a = b
            b = sum
            sum = a + b
        return hold


# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(FibonacciAdder(2) == 1))
print("Test 2 Passed: " + str(FibonacciAdder(5) == 7))
print("Test 3 Passed: " + str(FibonacciAdder(10) == 88))