#print the fibonacci series upto n terms#
n=int(input("Enter a number:"))
a=0
b=1
print("fibonacci series:")
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c

"""Input:Enter a number:7
Output:Fibonacci series:
0112358"""
