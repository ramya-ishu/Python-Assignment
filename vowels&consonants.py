#check the number of vowels and consonants in a string#
s=input("Enter string:")
vl=['a','e','i','o','u','A','E','I','O','U']
vs=0
cs=0
for i in s:
    if(ord(i)>=65 and ord(i)<=90)or(ord(i)>=97 and ord(i)<=122):
        if i in vl:
         vs+=1
        else:
         cs+=1
print(vs,cs)

"""Input:Enter a string:srilakshmiramya
Output: 5 10 """
