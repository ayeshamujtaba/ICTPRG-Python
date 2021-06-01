l1= []
items = input("Enter an item or press x to exit ")
while (items != 'x'):
    l1.append(items)
    items = str (input("Enter an item or press x to exit "))
print ("The shopping list" + str (l1))