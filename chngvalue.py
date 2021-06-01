def main():
    value =29
    print('value' ,value)
    change_value(value)
    print('Back in the function')
    print('value:' , value)

def change_value(number):
    print("number: ", number)
    print("number (input argument) changed:")
    number = 0
    print("number:", number)

main()