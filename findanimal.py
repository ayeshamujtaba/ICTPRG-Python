animals = ["cat", "dog", "panther", "fish", "pink panther"]

x = input("Enter animal to search: ")

i = 0

found = False

while i < len(animals):

    if x == animals[i]:

        print( "found " + x)

        found = True

    i = i+1

if found == False:

    print("Not found")