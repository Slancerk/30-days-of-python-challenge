from array import *                          #importing everything from array library to use array

arr = array('i',[])                          #declaring array of integers 

n = int(input("size of the array"))          #length of the array

for i in range(n):                           #to take array input from users
    x=int(input("enter the next number"))
    arr.append(x)                            #add element in the array
    i+=1

#print(arr)                                   


#for i in range(0,len(arr)):                  # range 0 index to last index of array
#    print(arr[i])
    
# take an element as a user input and check if present in the array

element=int(input("enter the number to check"))
m=0
for i in range(len(arr)):
    if element==arr[i]:
        print(f'found {arr[i]} at index {m}')
        break
    m+=1
        

else:
    print("not found")

