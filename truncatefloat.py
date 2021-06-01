import math 
print(math.pi) 
def truncate(num, n): 
    return int(num * (10**n))/(10**n) 
for k in range(6): 
    print( truncate(math.pi,k)) 
    # Try printing in columns # with "\t" the tab character print() print("k2\tTruncated pi") for k2 in range(6): msg = str(k2)+"\t" + str(truncate(math.pi,k2)) print(msg)
