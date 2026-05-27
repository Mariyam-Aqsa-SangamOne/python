list1=[]
list2=[]
list3=[]
list4=[]
for i in range(65,65+26,1):
    list1.append(i)

for i in range(97,97+26,1):
    list2.append(i)

for i in range(0,26,1):
    list3.append(chr(list1[i]))
    list4.append(chr(list2[i]))
print(list3)
print(list4)
