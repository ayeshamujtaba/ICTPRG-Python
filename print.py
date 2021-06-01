
#USE OF FORMAT SPECIFIERS
#printing a string
mystring = 'abc'
print("%s" % mystring)
days =31
#printing an integer
print("%d" % days )

#printing a float
cost = 189.4
print("%.2f"  % cost)

#printing adaptions with concatination
print("%s" % mystring + "%f" % cost)

#Date
# 2021-05-25

print("%d-" % 2021 + "0%d-" % 5 + "%d" % 25 )