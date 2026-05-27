list1=[2,4,6,8,10]#list
tuple1=(1,3,5,7)#tuple
set1={"north","south","east","west"}#set
dict1={1:"one",2:"two",3:"three"}#dictionary

len1=len(list1)
print(len1)
list1.append(12)
list1.append(14)
len1=len(list1)
print(len1)

len2=len(tuple1)
print(len2)
#tuple1.append(9) not allowed

print(set1)
set1.add("north")
print(set1)

print(dict1.keys())
print(dict1.values())
print(dict1.items())
