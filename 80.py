count=100
lucky=[]
prisons=['C']*count
print("Opening :",prisons)

for i in range(0,count,1):
    prisons[i]="O"
print("Round 1 :",prisons)

for i in range(1,count,2):
    prisons[i]="C"
print("Round 2 :",prisons)

for j in range(2,count,1):
    for i in range(j,10,j+1):
        if prisons[i]=="C":
            prisons[i]="O"
        else:
            prisons[i]="C"
    print("Round",j+1,":",prisons)

for i in range(0,count,1):
    if prisons[i]=="O":
        lucky.append(i+1)
print(lucky,"are the lucky prisoners")

    
#start,stop,step
#2,5,1
