names=[]
english=[]
toppersEng=[]
f1=open("marks.txt","r")

for i in range(0,26,1):
    s1=f1.readline()
    list1=s1.split(",")
    names.append(list1[0])
    list2=list1[3].split(":")
    english.append(list2[1])
maxEng=max(english)
print(maxEng)

for i in range(0,26,1):
    if english[i]==maxEng:
        toppersEng.append(names[i])
print("Toppers in English are:",toppersEng[0],"and",toppersEng[1],"with marks",maxEng)
#toppers in eng are latha and padma
