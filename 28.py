prisons=['C','C','C','C','C','C','C','C','C','C']
print("Opening:",prisons)
for i in range(0,10,1):
    prisons[i]='O'
print("Round 1:",prisons)
for i in range(1,10,2):
    prisons[i]="C"
print("Round 2:",prisons)

for i in range(2,10,3):
    if prisons[i]=="C":
        prisons[i]="O"
    else:
        prisons[i]="C"
print("Round 3:",prisons)

for i in range(3,10,4):
    if prisons[i]=="C":
        prisons[i]="O"
    else:
        prisons[i]="C"
print("Round 4:",prisons)

for i in range(4,10,5):
    if prisons[i]=="C":
        prisons[i]="O"
    else:
        prisons[i]="C"
print("Round 5:",prisons)
