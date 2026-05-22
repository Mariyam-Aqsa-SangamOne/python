def diamond2(word):
    n=len(word)

    for i in range(1,n+1,1):
        spaces=" "*(n-i)
        print(" "*(n-i)+word[:i])

    for i in range(n-1,0,-1):
        print(" "*(n-i)+word[:i])
diamond2("Funwith")
