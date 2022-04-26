def do_flames(name1,name2):

    string1 = name1.replace(" ","").lower() 
    string2 = name2.replace(" ","").lower() 

    name1  = list(string1)
    name2 = list(string2)


    for x in str(name1):
        if x in  name2:
            name1.remove(x)
            name2.remove(x)

    length = len(  name1 + name2) 
    arr = ["f","l","a","m","e","s"]
    flames = {
        "f" : "Friendship",
        "l":"Love",
        "a" : "Affection",
        "m" : "Marriage",
        "e" : "Enemy",
        "s" : "Sister",
    }

    def  array_split(arr,p)->list:
        arr1 = arr[:p] 
        arr2 = arr[p:] 
        
        return arr2  +  arr1   


    def loop(arr,counter):
        index = 0
        for _ in range(1,counter):
            if index     == len(arr)-1 :
                index = 0
            else:
                index += 1
        return index 

    while True:
        if ( len(arr) - 1) == 0:
            break
        
        index = loop(arr,length) 
        arr.pop(index)
        arr = array_split(arr,index)

    result ="".join(arr)
    return flames[result]

# print(do_flames("vignesh shivan","nayanthara"))


