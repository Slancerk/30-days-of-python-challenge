from array import *

n = int(input())
arr = array('i',[])
    
for i in range(n):
    x = int(input())
    arr.append(x)
        
maximum= max(arr)
arr.remove(maximum)

max2=max(arr)
 
print("runner up is ",max2)


# max=0
# for value in arr:
#     if value>max:
#         max=value
    
# arr.remove(max)
# print(arr)

    