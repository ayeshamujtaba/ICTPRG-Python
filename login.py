username = []
password =[]
loginfile = open ("login.txt" ,'r')
#content = loginfile.read()
#print(content)

def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele  
    return str1

testname = str(input("Enter username: "))
testpassword = str (input("Enter password: "))
#------------------------------------------
def searchloginfile(filename, stringtosearch):
    list_of_results = []
    with open(filename, 'r') as read_obj:
        for line in read_obj:
            if stringtosearch in line:
                list_of_results.append((line.rstrip()))
    return list_of_results

#------------------------------------------

#------------------------------------------
def check_line_number (filename, stringtosearch):
    linenumber = 0
    with open (filename, 'r') as read_obj:
        for line in read_obj:
            if stringtosearch in line:
                linenumber = linenumber +1
    return linenumber

result = searchloginfile ('login.txt', testname)
print (result)
passresult = searchloginfile ('login.txt', testpassword)
usercheck =listToString(result)
print(usercheck)
userlinecheck = check_line_number ('login.txt' ,testname)
passwordlinecheck = check_line_number ('login.txt', testpassword)
if userlinecheck == passwordlinecheck:
    print ("Access Granted")
else:
    print ("Access Denied")
count = len(usercheck)
for j in range (count -1):
    if usercheck[j] == ':':
        break
    else:
        username.append(usercheck[j])


name = listToString(username)
#print (name)
if testname == name:
    y = count -1
    while usercheck[y] != ':':
        password.append(usercheck[y])
        y = y-1
    passwd = listToString (password)
    passwdcorrect = passwd [::-1]
    print ("Access Granted! The Password is:", passwdcorrect , end ='')
else:
    print("Access Denied")

