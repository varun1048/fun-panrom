import os

os.system("cls")

name1  = list("surya")
name2 = list("jyothika")

# name1  = list("abc")
# name2 = list("efa")

for x in str(name1):
    if x in  name2:
        name1.remove(x)
        name2.remove(x)

# print(name1 + name2)
length = len(  name1 + name2) 
# print("length " , length) 

arr = ["F","L","A","M","E","S"]
print(arr)
# arr = ["f"]
flames = {
    "f" : "friendship",
    "l":"love",
    "a" : "affection",
    "m" : "marriage",
    "e" : "enemy",
    "s" : "sister",
}

def  array_split(arr,p)->list:
    arr1 = arr[:p] 
    arr2 = arr[p:] 
    
    return arr2  +  arr1   


length = 9
def loop(arr,counter):
    index = 0
    for _ in range(1,counter):
        print(index)
        if index     == len(arr)-1 :
            index = 0
        else:
            index += 1
    return index 

while True:
    if ( len(arr) - 1) == 0:
        break
    
    index = loop(arr,length) 
    print(f"index {index}")
    pop =  arr.pop(index)
    print(f"poped {pop}\n"  )
    arr = array_split(arr,index)
    print(arr)
    # i +=1









# def loop(arr,lenght ):
#     print({"arr":arr,"lenght":lenght},end="\n\n")

#     if lenght == len(arr):
#         print("one")
#         removed = arr.pop(lenght-1)
    
#     elif lenght < len(arr):
#         print("two")
#         removed =  arr.pop(lenght-1)
    
#     else:
#         print("three")
#         temp = (lenght - 1) - len(arr)
#         removed = arr.pop(temp)
    
#     print(removed)
#     return arr
    









# def loop(arr,length):
#     if len(arr) == 1:
#         return arr
    
#     index = 1
#     for _ in range(1,length+1):
#         for i , v  in enumerate(arr):
#             i += 1
                
#             # print((i,index))
#             if length == index:
                
#                 # arr.pop(i)
#                 print(v)
#                 return  
                
#             index += 1
#         print()
        
    
#     print()
#     print(index)
    
    
#     # return arr
