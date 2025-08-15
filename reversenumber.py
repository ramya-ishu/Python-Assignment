#Reverse the digits of a given number#
n=int(input("Enter a number:"))
rev=0
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print("reversed number is:",rev)
"""Input:Enter a number:123
Output:reversed number is:321""" 
