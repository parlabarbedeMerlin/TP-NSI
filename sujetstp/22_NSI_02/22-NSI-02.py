def moyenne(notes):
    l1=0
    l2=0
    for i in notes:
        l1+=i[0]*i[1]
        l2+=i[1]
    return l1/l2

print(moyenne([(15,2),(9,1),(12,3)]))

def pascal(n):
    C= [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i])
        Ck.append(1)
        C.append(Ck)
    return C

print(pascal(4))
