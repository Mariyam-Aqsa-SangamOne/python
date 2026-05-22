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
diamond3("Funwith")
