values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45, 78]
length = len (values)
number = max (values)
add = sum (values)
avg = float (add) / length
print ("The sum is:\t\t" ,add)
print ("The average is:\t\t" ,avg)
print ("The maximum number: is\t", number)
def cal_average(num):

    sum_num = 0

    for t in num:

        sum_num += t           

    avg = sum_num / len(num)

    return avg
print ("The average is" , cal_average(values))

