def genOtp1(n):
    import random as rd
    rdn=rd.randint(10**(n-1),10**n-1)
    print(rdn)
genOtp1(4)
genOtp1(6)
genOtp1(8)
