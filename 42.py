names=[]
f1=open("marks.txt","r")

s1=f1.readline()
list1=s1.split(",")
names.append(list1[0])

s1=f1.readline()
list2=s1.split(",")
names.append(list2[0])

s1=f1.readline()
list2=s1.split(",")
names.append(list2[0])

print(names)
