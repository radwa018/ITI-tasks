#1
def in_range(n, low=-5, high=5):
    return low < n < high
print(in_range(3))  
print(in_range(-6)) 

#2
def lists_to_dict(keys,values):
    return dict(zip(keys,values))
list1 = ["a","b","c"]
list2 = [1,2,3]
print(lists_to_dict(list1,list2))   

#3
def squares():
    result=[]
    for i in range(1,31):
        result.append(i**2)
    print(result)
squares()
#4
nums = [3, 6, 4, 0, 8]
#remove last element:
nums.pop()
#add R in the 2nd place (index 1):
nums.insert(1, 'R')
#ask user for number to delete:
delete_val = input("enter a value to delete from list:")
#convert to int if it's a number:
if delete_val.isdigit():
    delete_val=int(delete_val)
if delete_val in nums:
    nums.remove(delete_val)
else:
    print("Value not found in list!")

print("final list:", nums)

#5
def merge_dicts(d1, d2):
    merged=d1.copy() 
    for k, v in d2.items():
        if k not in merged: 
            merged[k]=v
    return merged

dict1 = {"a":1,"b": 2}
dict2 = {"b":5,"c": 3}
print(merge_dicts(dict1, dict2)) 
