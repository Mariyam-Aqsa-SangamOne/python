list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
for i in range(65,65+26,1):
    list1.append(i)

for i in range(97,97+26,1):
    list2.append(i)

for i in range(0,26,1):
    list3.append(chr(list1[i]))
    list4.append(chr(list2[i]))

for i in range(0,26,1):
    list5.append(ord(list3[i]))
    list6.append(ord(list4[i]))
print(list5)
print(list6)
