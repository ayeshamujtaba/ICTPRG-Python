age = int (input("Enter age:"))
hasMem = input ("Do you have membership y or Y")
hasMembership = (hasMem == "y" or hasMem == "Y")
hasMembership == False
if (hasMembership == True):
    if(age>=18):
        print("You may enter the private club")
    else:
        print("You may enter the playground")
else:
    if (age >= 18):
        print("You need a memebership before entering")
    else:
        print("You need a membership before entering playground")
