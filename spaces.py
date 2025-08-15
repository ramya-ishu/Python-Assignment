#Remove all spaces from a given string#
s=input("Enter a string:")
res=""
res1=""
for i in s:
    if i.isspace():
        res+=i
    else:
        res1+=i
print(res+res1)

"""Input:Enter a string:sri lakshmi ramya
Output:srilakshmiramya"""
