list1=[]
list2=[]
list3=[]
list4=[]

f1=open("GK1.txt","r")
for i in range(0,10,1):
    n1=f1.readline()
    n1=n1.strip()
    l1=n1.split(",")
    list1.append(l1[0])
    list2.append(l1[1])

f1.close()
for i in range(0,10,1):
    q1="What is the capital of "+list1[i]
    ans=input(q1+"?")
    list3.append(ans)
print()

for i in range(0,10,1):
    if list3[i].lower()==list2[i].lower():
        list4.append(10)
    else:
        list4.append(0)
print()

total=sum(list4)

print("countries:",list1)
print("Capitals:",list2)
print("Responses:",list3)
print("Marks:",list4)
print("Total marks:",total)

print("Wrongly Answered Questions:")
for i in range(0,10,1):
    if list4[i]==0:
        print("What is the capital of ",list1[i],"?")
        print("Correct answer: ",list2[i])
        print()
print()
