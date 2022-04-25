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
print("length " , length) 

arr = ["f","l","a","m","e","s"]
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


    
def loop(arr,counter):
    index = 0
    result = []
    
    for _ in range(1,counter + 1):
        try:
            result.append(arr[index])
        except:
            index = 0
            result.append(arr[index])
        index += 1
    # return { "value" :result.pop() ,"index" :index}
    print({"value" :result.pop()})
    return index

for x in range(0,length):
    index = loop(arr,length) 
    arr.pop(index) 
    print(array_split(arr,index))
    arr = array_split(arr,index)




ty = "".join(arr)
print( flames[ty]  )


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
