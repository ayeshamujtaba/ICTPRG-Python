string1 = 'one two three four five'
if 'four' in string1:
    print("Found" + " four" + " in " + string1)
else:
    print("The string four was not found")

print()
s1 = "123"
#Is it a digit
print(s1.isdigit())
#Is it a alpha numeric
print (s1.isalnum())
#Does it have space
print (s1.isspace())
#Is it upper case
print (s1.isupper())
#Is lower case
print (s1.islower())
#Split
print(s1.split())
