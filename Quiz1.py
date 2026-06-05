def quiz(fname):
    countries=[]
    capitals=[]
    responses=[]
    marks=[]

    f1=open(fname,"r")
    for i in range(0,10,1):
        s1=f1.readline()
        n1=s1.strip()
        l1=n1.split(",")
        countries.append(l1[0])
        capitals.append(l1[1])

    f1.close()
    for i in range(0,10,1):
        q1="What is the capital of "+countries[i]
        ans=input(q1+"?")
        responses.append(ans)
    print()

    for i in range(0,10,1):
        if responses[i].strip().lower()==capitals[i].strip().lower():
            marks.append(10)
        else:
            marks.append(0)
    print()

    total=sum(marks)
    print("Total marks:",total)
    if(total==100):
        print("Congratulations!")
    else:
        print("Wrongly Answered Questions:")
        for i in range(0,10,1):
            if marks[i]==0:
                print("What is the capital of ",countries[i],"?")
                print("Correct answer: ",capitals[i])
                print()
        print()
quiz("GK1.txt")
