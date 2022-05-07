def nameReplacer(name):
    return name.replace(" ", "").lower()

def makeListOfNames(name):
    return list(nameReplacer(name))

def do_flames(name1,name2):

    firstName = makeListOfNames(name1)
    secondName = makeListOfNames(name2)

    for x in str(firstName):
        if x in  secondName:
            firstName.remove(x)
            secondName.remove(x)

    length = len(firstName + secondName) 
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


