#def reverse_name (first, last): 
 #       print(last,first)

first_name = input("Enter your first name: ")
last_name = input ("Enter your last name: ")
#print ("your reversed name is")
#reverse_name(first_name,last_name)

#return "Smith Fred from revered_name2('Fred','Smith)"
def reverse_name2(first,last):
    s = last
    s+= " "
    s+= first
    return s



msg= "Your reversed name is "
msg +=reverse_name2('Fred','Smith')
print(msg)
#a = reverse_name2 ('Fred' , 'Smith')
#print (a)
print("your name reversed is: " + reverse_name2(first_name,last_name))