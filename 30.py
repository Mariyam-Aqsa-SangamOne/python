prisons=['C','C','C','C','C','C','C','C','C','C']
lucky=[]
print("Opening :",prisons)
for i in range(0,10,1):
    prisons[i]='O'
print("Round 1 :",prisons)
for i in range(1,10,2):
    prisons[i]="C"
print("Round 2 :",prisons)
for j in range(2,10,1): 
    for i in range(j,10,j+1):
        if prisons[i]=="C":
            prisons[i]="O"
        else:
            prisons[i]="C"
    print("Round",j+1,":",prisons)
for i in range(0,10,1):
    if prisons[i]=="O":
        lucky.append(i+1)
print(lucky,"are the lucky prisoners")
