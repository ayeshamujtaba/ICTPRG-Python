def get_fullname():
    first_name = input ("Enter first name: ")
    last_name = input ('Enter last name: ')
    return first_name,last_name

first,last = get_fullname()
print("The first name is", first)
print("The last name is", last)