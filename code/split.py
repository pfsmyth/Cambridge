# string.split()

mystring = "5,GER,17,10,15,42,View medals by sport for Germany"

mylistofitems = mystring.split(",")

print(mylistofitems)

print(mylistofitems[1])

for item in mylistofitems :
    print(item)

for item in mylistofitems :
    print(type(item))
