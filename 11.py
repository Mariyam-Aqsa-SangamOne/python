f1=open("in2.txt","r")
f2=open("out1.txt","w")
s1=f1.readline()
list1=s1.split(",")
print(list1)
num1=int(list1[0])
num2=int(list1[1])
for j in range(num1,num2+1,1):
    for i in range(1,11,1):
        print(j,i,j*i)
        f2.write("Aqsa")
    print()
f2.close()
