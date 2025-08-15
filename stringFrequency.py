#Count the frequency of each character in a string#
s=input("Enter a string:")
fre=""
for ch in s:
    if ch not in fre:
        count=0
        for c in s:
            if c==ch:
                count+=1
        print(ch,":",count)
        fre=fre+ch
"""Input:Enter a string:ramya
Output:
r:1
a:2
m:1
y:1"""

