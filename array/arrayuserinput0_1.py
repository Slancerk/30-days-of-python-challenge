from array import *                          #importing everything from array library to use array

arr = array('i',[])                          #declaring array of integers 

n = int(input("size of the array"))          #length of the array

for i in range(n):                           #to take array input from users
    x=int(input("enter the next number"))
    arr.append(x)                            #add element in the array
    i+=1

print(arr)                                   

for i in range(0,len(arr)):                  # range 0 index to last index of array
    print(arr[i])
    



