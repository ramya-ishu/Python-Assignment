#Reverse a given string without using built-in reverse functions#
string=input("Enter a string:")
l=len(string)
i=l-1
while i>=0:
    print(string[i],end='')
    i-=1

"""Input:Enter a string:Hello
Output:olleh"""
