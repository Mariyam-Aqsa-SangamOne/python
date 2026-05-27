def read_file():
    f1=open("GK1.txt","r")
    for i in range(0,10,1):
        n1=f1.readline()
        n1=n1.strip()
        l1=n1.split(",")
        list1.append(l1[0])
        list2.append(l1[1])

    f1.close()

def display_ques():
    for i in range(0,10,1):
        q1="What is the capital of "+list1[i]
        ans=input(q1+"?")
        list3.append(ans)
    print()

def check_ans():
    for i in range(0,10,1):
        if list3[i].lower()==list2[i].lower():
            list4.append(10)
        else:
            list4.append(0)

def display_result():
    total=sum(list4)
    print()
    print("Total marks:",total)
    print()
    print("Wrongly Answered Questions:")
    for i in range(0,10,1):
        if list4[i]==0:
            print("What is the capital of ",list1[i],"?")
            print("Correct answer: ",list2[i])

#Main 
list1=[]
list2=[]
list3=[]
list4=[]
read_file()
display_ques()
check_ans()
display_result()
