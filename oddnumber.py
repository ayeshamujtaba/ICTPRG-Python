def is_odd(number):
    if(number % 2) !=0:
        status = True
    else:
        status =False
    return status
def is_odd_print(number):
    print(str(number) + ":" +str(is_odd(number)))


print(is_odd(2))
print(is_odd(3))
print(is_odd(4))
is_odd_print(2)

    