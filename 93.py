def genOtp2(n,qty):
    def genOtp1(n):
        import random as rd
        rdn=rd.randint(10**(n-1),10**n-1)
        print(rdn)
    for i in range(0,qty,1):
        genOtp1(n)
genOtp2(4,10)
genOtp2(6,8)
genOtp2(8,4)
