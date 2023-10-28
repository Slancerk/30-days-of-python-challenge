#find average in an array

from array import *

arr=array('i',[])

num = int(input('enter the array size'))

for i in range(num):
    x=int(input('enter the element'))
    arr.append(x)

print(arr)

sum=0
for i in range(num):
    sum=sum+arr[i]


print(sum)
a=sum/num
print(f'average is ',a) 