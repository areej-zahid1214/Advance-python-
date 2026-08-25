tup=(67,44,65,23,55,67,35)
i=1
x=23
while i<len(tup):
    if tup[i]==x:
        print("found",i)
    else:
        print("There is no number")
    i+=1