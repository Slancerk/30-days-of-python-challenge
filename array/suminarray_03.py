# basically we will add all the elements in an array

from array import *

arr= array('i',[])
n = int(input('enter the length of the array'))

#array input
for i in range(n):
    x=int(input('enter the element')) 
    arr.append(x)
    i+=1

#array elements sum using for loop
# sum =0
# for i in range(len(arr)):     # i== index && arr[i] == number present in that index
#     sum = sum+arr[i]
#     i+=1
# print(f'the sum of all the elements in array is {sum}')


#we can do the similar thing using a simple function
add=int (sum(arr))
print(f"the sum of all the elements is {add}")