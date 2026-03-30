import pandas as pd


def dictValue(dict_param,key,default):
    if key not in dict_param:
        return default
    else :
        return dict_param[key]

def evenInList(lst):
    count = 0 
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            count += 1
    return count 


def largestInList(lst):
    largestYet = float('-inf')
    for i in range(len(lst)):
        if lst[i] > largestYet:
            largestYet = lst[i]
    return largestYet

def filterDataFrame(db:pd.DataFrame,column_name,column_value):
    
    v = db[db[column_name] == column_value]
    vLen = len(v)
    return v,"This many filtered rows:",vLen

def sumGreatThan(lst,target):
    
    total = 0
    newLst = []
    
    for i in range(len(lst)):
        total += lst[i]
        newLst.append(lst[i])
        if total >= target:
            break
        
    return total,newLst
 
    
        
    
    
    
    
    
    
    

print(largestInList([1,2,3,4,5,6,7,8,9,101,21,2323,145]))
test_dict = {
    "apple": 5,
    "banana": 8,
    "orange": 3
}
print(dictValue(test_dict,"banana",0))

print(evenInList([1,2,3,4,5,6,7,8,9,101,21,2323,100]))


test_db = pd.DataFrame([
    ["yes", "italian", "pos"],
    ["no",  "french",  "neg"],
    ["yes", "greek",   "neg"],
    ["no",  "italian", "pos"],
    ["yes", "french",  "pos"]
], columns=["veg", "type", "class"])

print(filterDataFrame(test_db,'type','italian'))

print(sumGreatThan([1,2,3,4,5,6,7,8,9,101,21,2323,100],147))



