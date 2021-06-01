
with open("login.txt", "r") as f:
    lines = f.readlines()
print (lines)
newlist = [i.split('\n',1)[0] for i in lines]
print(newlist)
count=0
for line in newlist:
    # count = count + 1
    count += 1  
    format_list = ("{}".format(line.strip()))

x = 'Hello word'
print(x[2:])