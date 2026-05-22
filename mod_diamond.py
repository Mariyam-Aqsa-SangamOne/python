def diamond1(word1):
    for i in range(0,len(word1)):
        print(word1[:i])

    for i in range(len(word1)-1,0,-1):
        print(word1[:i])
    print()

def diamond2(word2):
    n=len(word2)
    for i in range(1,n+1,1):
        print(" "*(n-i)+ word2[:i])
        
    for i in range(n-1,0,-1):
        print(" "*(n-i)+word2[:i])
    print()

def diamond3(word3):
    n = len(word3)
    for i in range(1,n+1,1):
        print(" "*(n-i),end="")
        
        for j in range(i):
            print(word3[j],end=" ")
        print()

    for i in range(n-1,0,-1):
        print(" "*(n-i),end="")
        
        for j in range(i):
            print(word3[j],end=" ")

        print()
