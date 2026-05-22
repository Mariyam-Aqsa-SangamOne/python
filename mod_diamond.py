def diamond1(word):
    for i in range(1,len(word)+1,1):
        print(word[:i])

    for i in range(len(word)-1,0,-1):
        print(word[:i])

def diamond2(word):
    n=len(word)

    for i in range(1,n+1,1):
        spaces=" "*(n-i)
        print(" "*(n-i)+word[:i])

    for i in range(n-1,0,-1):
        print(" "*(n-i)+word[:i])

def diamond3(word): 
    n=len(word)
    for i in range(1, n+1):
        spaces=" "*(n-i)
        letters=" ".join(word[:i])
        print(spaces+letters)

    for i in range(n-1,0,-1):
        spaces=" "*(n-i)
        letters=" ".join(word[:i])
        print(spaces + letters)
