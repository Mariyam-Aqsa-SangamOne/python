def genOtp1(n):
    import random as rd
    rdn=rd.randint(10**(n-1),10**n-1)
    print(rdn)
for i in range(0,10,1):
    genOtp1(4)
