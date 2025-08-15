#check if a string is a palindrome#
s=input("Enter a string:")
rev=''
for i in s:
    rev=i+rev
if s==rev:
    print('palindrome')
else:
    print('not palindrome')

"""Input:Enter a string:madam
Output:palindrome"""
"""Input:Enter a string:ramya
Output:not palindrome"""
