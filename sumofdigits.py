#Find the sum of digits of a given number#
n=int(input("Enter a number:"))
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem
    n=n//10
print(sum)

"""Input:"Enter a number:1234
Output:10"""
